def print_models(unprinted_designs, completed_models):
    """
    Simulasi mencetak setiap desain sampai tidak ada yang tersisa.
    Pindahkan setiap desain ke completed_models setelah dicetak.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Lagi nge-print model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Tampilkan semua model yang sudah selesai dicetak."""
    print("\nIni dia model-model yang udah selesai dicetak:")
    for completed_model in completed_models:
        print(completed_model)