import pytest

from main import count_words_in_file

@pytest.fixture
def create_temp_file(tmp_path):
    def _create_file(name, content):
        file_path = tmp_path / name
        file_path.write_text(content, encoding='utf-8')
        return str(file_path)
    return _create_file

def test_empty_file(create_temp_file):
    file_path = create_temp_file("empty.txt", "")
    assert count_words_in_file(file_path) == 0

def test_single_word(create_temp_file):
    file_path = create_temp_file("one_word.txt", "Привіт")
    assert count_words_in_file(file_path) == 1

def test_multiple_words(create_temp_file):
    content = "Це приклад текстового файлу з кількома словами."
    file_path = create_temp_file("multi.txt", content)
    assert count_words_in_file(file_path) == 7

def test_file_not_found():
    assert count_words_in_file("does_not_exist.txt") == "Файл не знайдено"

def test_non_utf8_file(tmp_path):
    file_path = tmp_path / "non_utf8.txt"
    file_path.write_bytes("äöü".encode("latin1"))  # Зберігаємо в іншому кодуванні
    assert count_words_in_file(str(file_path)) == "Непідтримуване кодування файлу"