def send_messages(messages, sent_messages):
    """Mencetak setiap pesan lalu memindahkannya ke list pesan terkirim."""
    while messages:
        current_message = messages.pop(0)
        print(f"Lagi ngirim pesan: {current_message}")
        sent_messages.append(current_message)


texts = [
    "Halo semuanya! Lagi pada ngapain nih?",
    "Nanti malam jadi nongkrong kan?",
    "Jangan lupa bawa tugasnya ya!",
    "Makasih banget udah dibantuin tadi!",
]
sent_messages = []

send_messages(texts[:], sent_messages)

print("\nIsi list texts (list asli) sekarang:")
print(texts)
print("\nIsi list sent_messages sekarang:")
print(sent_messages)