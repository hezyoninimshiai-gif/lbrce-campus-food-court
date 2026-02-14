"""
Telegram Notification Service
=============================
Sends Telegram messages when order status changes.

This is NOT a separate bot service. It's just HTTP calls to the
Telegram Bot API using the `requests` library.

No `python-telegram-bot` library needed.
"""

# import requests
# from config import Config

# TELEGRAM_API_URL = f"https://api.telegram.org/bot{Config.TELEGRAM_BOT_TOKEN}/sendMessage"


def send_telegram_message(chat_id, message):
    """
    Send a message to a Telegram user.

    Args:
        chat_id (int): The user's Telegram chat ID (stored in users.telegram_id)
        message (str): The message text to send

    Steps:
    1. Build the Telegram API URL: https://api.telegram.org/bot<TOKEN>/sendMessage
    2. Send POST request with JSON body: { "chat_id": chat_id, "text": message }
    3. Check response status — log error if it fails
    4. Don't raise exceptions — notification failure should NOT break the order flow

    Note: If chat_id is None, skip sending (user hasn't linked Telegram).
    """
    pass


def notify_admin_new_order(order_id, user_name, stall_name, total_amount):
    """
    Notify admin(s) when a new order is placed.

    Args:
        order_id (int): The new order ID
        user_name (str): Name of the student who placed the order
        stall_name (str): Name of the food stall
        total_amount (float): Total order amount in rupees

    Steps:
    1. Query users table for all users with role = 'admin' and telegram_id IS NOT NULL
    2. Build message: "New order #{order_id} from {user_name} - {stall_name} - ₹{total_amount}"
    3. For each admin with a telegram_id, call send_telegram_message(admin.telegram_id, message)

    Note: If no admins have linked Telegram, this is a no-op (no error).
    """
    pass


def notify_order_approved(user_telegram_id, order_id, estimated_time=None):
    """
    Notify student when their order is approved.

    Args:
        user_telegram_id (int): Student's Telegram chat ID
        order_id (int): The order ID
        estimated_time (int, optional): Minutes until order is ready

    Steps:
    1. If user_telegram_id is None, return (user hasn't linked Telegram)
    2. Build message:
       - With time: "Your order #{order_id} has been approved! It will be ready in {estimated_time} minutes."
       - Without time: "Your order #{order_id} has been approved!"
    3. Call send_telegram_message(user_telegram_id, message)
    """
    pass


def notify_order_ready(user_telegram_id, order_id, stall_name):
    """
    Notify student when their order is ready for pickup.

    Args:
        user_telegram_id (int): Student's Telegram chat ID
        order_id (int): The order ID
        stall_name (str): Name of the food stall for pickup

    Steps:
    1. If user_telegram_id is None, return
    2. Build message: "Your order #{order_id} is ready for pickup at {stall_name}!"
    3. Call send_telegram_message(user_telegram_id, message)
    """
    pass


def notify_order_rejected(user_telegram_id, order_id, reason):
    """
    Notify student when their order is rejected.

    Args:
        user_telegram_id (int): Student's Telegram chat ID
        order_id (int): The order ID
        reason (str): Rejection reason from admin

    Steps:
    1. If user_telegram_id is None, return
    2. Build message: "Your order #{order_id} was rejected. Reason: {reason}"
    3. Call send_telegram_message(user_telegram_id, message)
    """
    pass
