from typing import Callable
import asyncio

from telethon import TelegramClient, events
from telethon.errors import (
    AlreadyInConversationError,
    BotInlineDisabledError,
    BotResponseTimeoutError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
    ChatSendStickersForbiddenError,
    FloodWaitError,
    MessageIdInvalidError,
    MessageNotModifiedError,
)

from .logger import logging
from config import Config
from .tg_manager import edit_delete


LOGS = logging.getLogger("MiniUserBot")


class MiniUserBotCient(TelegramClient):
    """Userbot client inherited from TelegramClient"""

    def client_cmd(
        self: TelegramClient,
        pattern: str | tuple | None = None,
        command: str | tuple | None = None,
        group_only: bool = False,
        private_only: bool = False,
    ) -> Callable:
        if command is not None:
            pattern = Config.COMMAND_HANDLER + command

        def decorator(func):
            async def wrapper(event):
                if group_only and not event.is_group:
                    return await edit_delete(
                        event, "`This command is only for groups.`", 10
                    )
                if private_only and not event.is_private:
                    return await edit_delete(
                        event, "`This command is only for private chat.`", 10
                    )
                try:
                    await func(event)
                except events.StopPropagation:
                    raise events.StopPropagation
                except KeyboardInterrupt:
                    pass
                except MessageNotModifiedError:
                    LOGS.error("Message was same as previous message")
                except MessageIdInvalidError:
                    LOGS.error("Message was deleted or cant be found")
                except BotInlineDisabledError:
                    await edit_delete(event, "`Turn on Inline mode for our bot`", 10)
                except ChatSendStickersForbiddenError:
                    await edit_delete(
                        event, "`I guess i can't send stickers in this chat`", 10
                    )
                except BotResponseTimeoutError:
                    await edit_delete(
                        event, "`The bot didnt answer to your query in time`", 10
                    )
                except ChatSendMediaForbiddenError:
                    await edit_delete(event, "`You can't send media in this chat`", 10)
                except AlreadyInConversationError:
                    await edit_delete(
                        event,
                        "`A conversation is already happening with the given chat. try again after some time.`",
                        10,
                    )
                except ChatSendInlineForbiddenError:
                    await edit_delete(
                        event, "`You can't send inline messages in this chat.`", 10
                    )
                except FloodWaitError as e:
                    LOGS.error(
                        f"A flood wait of {e.seconds} occured. wait for {e.seconds} seconds and try"
                    )
                    await event.delete()
                    await asyncio.sleep(e.seconds + 5)
                except BaseException as e:
                    LOGS.exception(e)

                return wrapper

            self.add_event_handler(
                wrapper, events.NewMessage(pattern=pattern, outgoing=True)
            )

        return decorator
