printed_lines = set()
def modern_print(text):
    if text not in printed_lines:
        print(text)
        printed_lines.add(text)

modern_print("ytyt")
modern_print("ytyt")
