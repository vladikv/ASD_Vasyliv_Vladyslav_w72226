def rabin_karp(text, pattern):
    pattern_length = len(pattern)
    pattern_ascii_sum = sum(ord(c) for c in pattern)
    pattern_hash = pattern_ascii_sum % 101

    print(f"{'Fragment':<10} {'Suma ASCII':<12} {'Hash (mod 101)':<15} {'Komentarz'}")

    for i in range(len(text) - pattern_length + 1):
        fragment = text[i:i+pattern_length]
        fragment_ascii_sum = sum(ord(c) for c in fragment)
        fragment_hash = fragment_ascii_sum % 101

        if fragment_hash == pattern_hash:
            if fragment == pattern:
                komentarz = "Dopasowanie"
            else:
                komentarz = "Hash pasuje, ale nie identyczne"
        else:
            komentarz = "Niepasujące"

        print(f"{fragment:<10} {fragment_ascii_sum:<12} {fragment_hash:<15} {komentarz}")


text = "thesunrisesatsunset"
pattern = "sun"

rabin_karp(text, pattern)