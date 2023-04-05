import aiogram
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from user_keyboards import *

async def start_request(message: types.Message, state: FSMContext):
    """
    Handler for the /start command from a user, initiates a new request.
    """
    # Get the user's ID and name
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    # Save the user's information in the state
    await state.update_data(user_id=user_id, user_name=user_name)

    # Generate and send the new request keyboard
    keyboard = generate_new_request_keyboard()
    await message.answer("What type of request would you like to make?", reply_markup=keyboard)

async def handle_new_request(message: types.Message, state: FSMContext):
    """
    Handler for a user selecting a new request option from the keyboard, prompts for additional information.
    """
    # Get the selected option and save it in the state
    request_type = message.text
    await state.update_data(request_type=request_type)

    # Prompt the user for more information
    await message.answer(f"Please provide more information about your {request_type} request.")

    # Move to the next state
    await NewRequest.next()

async def handle_request_info(message: types.Message, state: FSMContext):
    """
    Handler for a user providing additional information about their request, confirms and sends to operators.
    """
    # Get the user's ID and name from the state
    data = await state.get_data()
    user_id = data['user_id']
    user_name = data['user_name']

    # Get the request type and additional information from the message
    request_type = data['request_type']
    request_info = message.text

    # Generate a confirmation message
    confirmation_message = f"Your {request_type} request has been submitted:\n\n{request_info}"

    # Send the confirmation message to the user
    await message.answer(confirmation_message)

    # Send the request to the operators
    await send_request_to_operators(user_id, user_name, request_type, request_info)

    # Reset the state
    await state.finish()

async def handle_cancel(message: types.Message, state: FSMContext):
    """
    Handler for a user canceling a request, cancels the current state and sends a cancellation message.
    """
    await state.finish()
    await message.answer("Your request has been canceled.")
