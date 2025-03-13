def book_input(books):
    pass

def book_update(books):
    pass

def book_delete(books):
    if not books:
        print("경고: 삭제할 도서가 없습니다.")
        return
    
    remove_isbn = input("삭제할 도서의 ISBN을 입력하세요. >>> ").strip()
    
    def find_book_index(isbn):
        #ISBN을 기준으로 도서의 인덱스를 찾는 함수
        for index, book in enumerate(books):
            if book["ISBN"] == isbn:
                return index
        return None
    
    index = find_book_index(remove_isbn)
    
    if index is not None:
        print(f"'{books[index]['제목']}' 도서를 삭제하시겠습니까? 예 / 아니요 >>> ")
        answer = input("예 / 아니요: ").strip()
        
        if answer == '예':
            del books[index]
            print(f"'{remove_isbn}' 도서가 삭제되었습니다.")
        else:
            print("삭제를 취소합니다.")
    else:
        print("해당 ISBN의 도서를 찾을 수 없습니다.")

def book_search(books):
    search_type = input("검색할 기준을 선택하세요 (1: ISBN, 2: 제목, 3: 저자, Enter: 전체 목록) >>> ").strip()
    search_value = ""
    
    def filter_books(criteria, value):
        # 주어진 기준과 값에 따라 도서를 필터링하는 함수
        if criteria == "ISBN":
            return [book for book in books if book["ISBN"] == value]
        elif criteria == "제목":
            return [book for book in books if value.lower() in book["제목"].lower()]
        elif criteria == "저자":
            return [book for book in books if value.lower() in book["저자"].lower()]
        return books  # 전체 목록 반환
    
    if search_type == "1":
        search_value = input("검색할 ISBN을 입력하세요 >>> ").strip()
        found_books = filter_books("ISBN", search_value)
    elif search_type == "2":
        search_value = input("검색할 제목을 입력하세요 >>> ").strip()
        found_books = filter_books("제목", search_value)
    elif search_type == "3":
        search_value = input("검색할 저자를 입력하세요 >>> ").strip()
        found_books = filter_books("저자", search_value)
    else:
        found_books = books  # 전체 목록 출력
    
    if not found_books:
        print("❌ 검색된 도서가 없습니다.")
    else:
        print("\n📖 도서 목록")
        for i, book in enumerate(found_books, start=1):
            print(f"{i}. ISBN: {book['ISBN']} | 제목: {book['제목']} | 저자: {book['저자']} | 대여 여부: {'대여 중' if book['대여 여부'] else '대여 가능'}")


def book_rent(books):
    pass