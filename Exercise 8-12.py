def make_sandwich(*items):
    """Mencetak ringkasan sandwich berdasarkan bahan yang dipesan."""
    print("\nPesanan sandwich kamu lagi disiapin nih. Isinya:")
    for item in items:
        print(f"- {item}")


make_sandwich('telur')
make_sandwich('ayam crispy', 'selada', 'tomat')
make_sandwich('tuna', 'keju', 'jamur', 'mayones', 'saus sambal')