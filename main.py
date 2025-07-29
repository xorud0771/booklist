#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
도서 관리 시스템 메인 프로그램
=============================
도서관의 도서를 관리하기 위한 콘솔 기반 프로그램입니다.

기능:
1. 도서 추가 - 새로운 도서를 시스템에 등록
2. 도서 수정 - 기존 도서 정보 변경
3. 도서 삭제 - 시스템에서 도서 제거
4. 도서 검색 - 다양한 조건으로 도서 검색
5. 도서 대여/반납 - 도서 대여 상태 관리
6. 프로그램 종료

사용법:
    python main.py

작성자: 도서관 관리 시스템 팀
버전: 1.0
최종 수정일: 2024-01-XX
"""

import sys
import Book_Checking_func as library  # 도서 관리 함수 모듈 import

def display_header():
    """프로그램 시작 시 헤더 정보를 출력하는 함수"""
    print("=" * 60)
    print("📚 도서 관리 시스템 v1.0")
    print("=" * 60)
    print("도서관의 도서를 효율적으로 관리할 수 있는 시스템입니다.")
    print()

def display_menu():
    """메뉴를 출력하는 함수"""
    menu_text = '''
┌─────────────────────────────────────────────────────────┐
│                    📖 메뉴 선택                         │
├─────────────────────────────────────────────────────────┤
│  1. 📖 도서 추가        4. 🔍 도서 검색                │
│  2. ✏️  도서 수정        5. 📚 도서 대여/반납           │
│  3. 🗑️  도서 삭제        6. 🚪 프로그램 종료            │
└─────────────────────────────────────────────────────────┘
메뉴를 선택하세요 >>> '''
    return menu_text

def main():
    """
    메인 실행 함수
    프로그램의 전체 흐름을 제어하고 사용자 입력에 따라 적절한 함수를 호출합니다.
    """
    # 프로그램 시작 헤더 출력
    display_header()
    
    # 초기 도서 데이터 (예제 도서 포함)
    books = [
        {"ISBN": "0000", "제목": "파이썬 프로그래밍", "저자": "홍길동", "대여 여부": False},
        {"ISBN": "0001", "제목": "자료구조와 알고리즘", "저자": "김철수", "대여 여부": False},
        {"ISBN": "0002", "제목": "웹 개발 입문", "저자": "이영희", "대여 여부": True}
    ]
    
    # 메인 프로그램 루프
    while True:
        try:
            # 메뉴 출력 및 사용자 입력 받기
            menu = input(display_menu()).strip()
            
            # 메뉴 선택에 따른 기능 실행
            if menu == '1':  # 도서 추가
                print('\n📖 도서 추가')
                print('-' * 40)
                books = library.book_input(books)
                
            elif menu == '2':  # 도서 수정
                print('\n✏️ 도서 수정')
                print('-' * 40)
                if not books:
                    print("❌ 수정할 도서가 없습니다.")
                else:
                    books = library.book_update(books)
                    
            elif menu == '3':  # 도서 삭제
                print('\n🗑️ 도서 삭제')
                print('-' * 40)
                library.book_delete(books)
                
            elif menu == '4':  # 도서 검색
                print('\n🔍 도서 검색')
                print('-' * 40)
                library.book_search(books)
                
            elif menu == '5':  # 도서 대여/반납
                print('\n📚 도서 대여/반납')
                print('-' * 40)
                if not books:
                    print("❌ 대여할 도서가 없습니다.")
                else:
                    library.book_rent(books)
                    
            elif menu == '6':  # 프로그램 종료
                print('\n🚪 프로그램을 종료합니다.')
                print('도서 관리 시스템을 이용해 주셔서 감사합니다! 👋')
                sys.exit(0)
                
            else:  # 잘못된 메뉴 선택
                print("❌ 잘못된 메뉴 선택입니다. 1-6 사이의 번호를 입력해주세요.")
                
        except KeyboardInterrupt:
            # Ctrl+C 입력 시 프로그램 종료
            print('\n\n프로그램이 사용자에 의해 중단되었습니다.')
            print('도서 관리 시스템을 이용해 주셔서 감사합니다! 👋')
            sys.exit(0)
            
        except ValueError:
            # 잘못된 입력값 처리
            print("❌ 올바른 값을 입력해주세요.")
            
        except Exception as e:
            # 예상치 못한 오류 처리
            print(f"❌ 오류가 발생했습니다: {e}")
            print("프로그램을 다시 시작해주세요.")
            
        # 각 작업 후 구분선 출력
        print('\n' + '=' * 60)

if __name__ == "__main__":
    """
    스크립트가 직접 실행될 때만 main() 함수를 호출
    모듈로 import될 때는 실행되지 않음
    """
    main() 