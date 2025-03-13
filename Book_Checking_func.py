def book_input(books):
    while True:
        book_number = input(" 번호를 입력하세요(4자리로 설정하시오) >>> ")
        check = 0 # 중복확인
        for book in books :
            if book["ISBN"] == book_number: #번호가 존재하면
                check = 1 # 중복 확인 변수 변경
                print("중복된 번호입니다. 새로운 번호로 다시 입력하세요.")
                break # 중복 발견 시 루프 종료
            
        if check == 0:
            break
        
    book_title = input(" 제목을 입력하세요 >>> ")
    book_author = input(" 저자를 입력하세요 >>> ")

    books.append({"ISBN" : book_number, "제목" : book_title, "저자" : book_author, "대여 여부" : False})
    print("도서가 추가되었습니다.")
    return books

def book_update(books):
    pass

def book_delete(books):
    pass

def book_search(books):
    pass

def book_rent(books):
    pass