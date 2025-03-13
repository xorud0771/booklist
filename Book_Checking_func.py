def book_input(books):
    pass

def book_update(books):
        while True:
            # 도서 리스트 출력 (수정할 때마다 최신 리스트를 보여줌)
            print("\n현재 보유 중인 도서 리스트:")
            for i in range(len(books)):
                print(f"{i + 1}. {books[i]['제목']} (ISBN: {books[i]['ISBN']}, 저자: {books[i]['저자']}, 대여 여부: {books[i]['대여 여부']})")
            
            # 수정할 도서 번호 입력
            book_num = input('수정할 도서 번호 입력 > ').strip()

            if 1 <= int(book_num) <= len(books):
                book_num = int(book_num) - 1  # 인덱스는 0부터 시작하므로
                break
            else:
                print("해당 번호가 없습니다. 다시 입력해주세요.")

        while True:
            print("\n수정할 항목을 선택하세요:")
            print("1. ISBN")
            print("2. 제목")
            print("3. 저자")
            
            number = int(input('수정할 부분 > ').strip())

            if 1 <= number <= 3:
                break
            else:
                print("잘못된 번호입니다. 1~3 사이의 번호를 입력해주세요.")

        # 도서 수정 부분
        if number == 1:
            while True:
                new_isbn = input(f'새 ISBN을 입력하세요 (기존 ISBN: {books[book_num]["ISBN"]}): ').strip()
                
                # ISBN 중복 체크
                isbn_exists = False
                for book in books:
                    if book["ISBN"] == new_isbn:
                        isbn_exists = True
                        break
                
                if new_isbn == books[book_num]["ISBN"]:
                    print("ISBN이 기존과 동일합니다. 다시 입력하세요.")
                elif isbn_exists:
                    print("이미 존재하는 ISBN입니다. 다른 ISBN을 입력해주세요.")
                else:
                    books[book_num]["ISBN"] = new_isbn
                    print(f"ISBN이 수정되었습니다: {books[book_num]['ISBN']}")
                    break

        elif number == 2:
            new_title = input(f'새 제목을 입력하세요 (기존 제목: {books[book_num]["제목"]}): ').strip()
            books[book_num]["제목"] = new_title
            print(f"제목이 수정되었습니다: {books[book_num]['제목']}")

        elif number == 3:
            new_author = input(f'새 저자를 입력하세요 (기존 저자: {books[book_num]["저자"]}): ').strip()
            books[book_num]["저자"] = new_author
            print(f"저자가 수정되었습니다: {books[book_num]['저자']}")


        # 수정 후 최신 도서 정보 출력
        print(f"수정된 도서 정보: {books[book_num]}")
        return books

def book_delete(books):
    pass

def book_search(books):
    pass

def book_rent(books):
    pass