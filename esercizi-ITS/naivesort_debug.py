def naivesort_debug(arr):
    """
    Versione con debug per visualizzare il doppio ciclo.
    """
    n = len(arr)
    print(f"{'='*60}")
    print(f"LISTA INIZIALE: {arr}")
    print(f"{'='*60}\n")

    for i in range(n - 1):
        print(f"{'─'*60}")
        print(f"▶ Ciclo ESTERNO: i={i} — sistemo la posizione {i}")
        print(f"  Porzione non ordinata: {arr[i:]}")
        print(f"  Candidato corrente nella posizione {i}: {arr[i]}\n")

        idx_minimo = i

        for j in range(i + 1, n):
            print(f"    Ciclo INTERNO: j={j} → confronto {arr[j]} con minimo attuale {arr[idx_minimo]}", end="")
            if arr[j] < arr[idx_minimo]:
                print(f" ← NUOVO MINIMO! (era {arr[idx_minimo]})")
                idx_minimo = j
            else:
                print(f" ← nessun cambio")

        print(f"\n  ✅ Minimo trovato: {arr[idx_minimo]} alla posizione {idx_minimo}")

        if idx_minimo != i:
            print(f"  🔄 Scambio: arr[{i}]={arr[i]} ↔ arr[{idx_minimo}]={arr[idx_minimo]}")
            arr[i], arr[idx_minimo] = arr[idx_minimo], arr[i]
        else:
            print(f"  ℹ️  Nessuno scambio: {arr[i]} è già al posto giusto")

        print(f"  LISTA ORA: {arr}\n")

    print(f"{'='*60}")
    print(f"LISTA ORDINATA: {arr}")
    print(f"{'='*60}")
    return arr


# ── Test ──
if __name__ == "__main__":
    dati = [64, 34, 25, 12, 22, 11, 90]
    naivesort_debug(dati)
