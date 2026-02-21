"""
Python 3 エンジニア認定実践試験 早見表生成スクリプト
各モジュールの print() 出力を「早見表.txt」に書き出します。
"""
import subprocess
import sys
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 実行するモジュール一覧（フォルダ, ファイル名）
# ※ timedeltaModule は dateModule / datetimeModule / timeModule を import するため最後に実行
MODULES = [
    ("collectionsModule", "counterModule.py"),
    ("collectionsModule", "defaultDictKeyModule.py"),
    ("collectionsModule", "namedtupleModule.py"),
    ("collectionsModule", "orderdDictModule.py"),
    ("copyModeule",       "copyModule.py"),
    ("enumModule",        "enumModule.py"),
    ("itertoolsModule",   "itertoolsModule.py"),
    ("sortModule",        "operatorModule.py"),
    ("sortModule",        "reversedModule.py"),
    ("sortModule",        "sortedModule.py"),
    ("sortModule",        "sortModule.py"),
    ("timeModule",        "timeModule.py"),
    ("timeModule",        "dateModule.py"),
    ("timeModule",        "datetimeModule.py"),
    ("timeModule",        "culculationTimeModule.py"),
    ("timeModule",        "timedeltaModule.py"),
]

# ANSI エスケープコード（colorama のカラー出力）を除去する正規表現
ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

output_path = os.path.join(BASE_DIR, "早見表.txt")

with open(output_path, "w", encoding="utf-8") as out_file:
    out_file.write("Python 3 エンジニア認定実践試験 早見表\n")
    out_file.write("=" * 60 + "\n\n")

    for folder, filename in MODULES:
        module_dir = os.path.join(BASE_DIR, folder)
        module_path = os.path.join(module_dir, filename)
        section_title = f"{folder}/{filename}"

        out_file.write(f"\n{'=' * 60}\n")
        out_file.write(f"  {section_title}\n")
        out_file.write(f"{'=' * 60}\n")

        # PYTHONUTF8=1 で子プロセスの入出力を UTF-8 に統一する
        env = os.environ.copy()
        env["PYTHONUTF8"] = "1"
        env["PYTHONIOENCODING"] = "utf-8"

        result = subprocess.run(
            [sys.executable, module_path],
            capture_output=True,
            cwd=module_dir,
            env=env,
        )

        # stdout/stderr をバイト列として受け取り UTF-8 でデコード（変換不能文字は置換）
        raw_stdout = result.stdout.decode("utf-8", errors="replace") if result.stdout else ""
        clean_stdout = ANSI_ESCAPE.sub("", raw_stdout)
        out_file.write(clean_stdout)

        if result.returncode != 0 and result.stderr:
            raw_stderr = result.stderr.decode("utf-8", errors="replace")
            clean_stderr = ANSI_ESCAPE.sub("", raw_stderr)
            out_file.write(f"\n[エラー]\n{clean_stderr}\n")

print(f"早見表を生成しました: {output_path}")
