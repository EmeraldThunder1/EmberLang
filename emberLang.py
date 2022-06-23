import src.lexer as lexer
import src.compiler as compiler
import sys
import time

file = "test.ember"
out = "out"

with open(sys.argv[1] if not file else file, 'r') as f:
    code = f.read()
    f.close()
    

code = """Stage {
            global test = 'Hello World'
            @on_flag () {
                
            }
        }
        Sprite Test {
            var hello = 'Hello World'
            
            @on_flag () {
                set_costume("logo.png")
                hide()
            }
        }"""

print("Tokenizing...")
start = time.time()

_lexer = lexer.Lexer()
tokens = _lexer.lex(code)

print(f"Finished tokenizing in {time.time() - start} seconds.")

print("Compiling...")

_compiler = compiler.Compiler(out)
_compiler.compile(tokens)

print(f'Finished compiling in {time.time() - start} seconds.')
