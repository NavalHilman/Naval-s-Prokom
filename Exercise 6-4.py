glossary = {
    'variable': 'tempat buat nyimpen data biar bisa dipakai lagi nanti.',
    'string': 'teks yang ditulis di dalam tanda kutip.',
    'list': 'kumpulan data berurutan yang ditulis di dalam kurung siku.',
    'loop': 'cara bikin Python ngulang perintah tanpa capek.',
    'dictionary': 'kumpulan data berpasangan antara kunci dan nilainya.',
    'integer': 'angka bulat tanpa titik desimal.',
    'float': 'angka yang punya bagian desimal.',
    'boolean': 'nilai yang cuma bisa True atau False.',
    'function': 'blok kode yang bisa dipanggil berkali-kali biar nggak nulis ulang.',
    'comment': 'catatan kecil di kode yang diabaikan sama Python.',
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n    {meaning}\n")