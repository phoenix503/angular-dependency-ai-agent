def print_report(results):
    print("\nDependency Analysis Report\n")
    for r in results:
        print(
            f"{r['package']:<25} "
            f"{r['current']:<10} → {r['latest']:<10} "
            f"{r['recommendation']}"
        )
