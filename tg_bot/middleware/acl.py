from aiogram.dispatcher.middlewares import BaseMiddleware
# from aiogram import types
#
#
# class ACLMiddleware(BaseMiddleware):
#     async def setup_chat(self, data: dict, user: types.User):
#         user_id = user.id
#         user = User()
#
#     async def on_pre_process_message(self, message: types.Message,
#     data: dict):
#         await self.setup_chat(data, message.from_user)
#
#     async def on_pre_process_callback_query(
#         self, call: types.CallbackQuery, data: dict
#     ):
#         await self.setup_chat(data, call.from_user)
