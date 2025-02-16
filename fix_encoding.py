#!/usr/bin/env python3
import sys
import ftfy

def fix_text_file(input_path, output_path):
    # 入力ファイルを読み込み（エンコーディングは一旦UTF-8で読み込みますが、必要に応じて変更してください）
    with open(input_path, 'r', encoding='utf-8', errors='replace') as infile:
        original_text = infile.read()
    
    # ftfy を使って文字化け（mojibake）を修正
    fixed_text = ftfy.fix_text(original_text)
    
    # 修正後のテキストを出力ファイルに書き出し
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(fixed_text)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python fix_encoding.py input_file output_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    fix_text_file(input_file, output_file)
    print(f"文字化け修正完了！\n出力ファイル: {output_file}")

