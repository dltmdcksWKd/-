# #while문 특정 조건을 만족 시킬떄까지 반복 재생
# treehit=0
# while treehit < 999999:                         #조건
#     treehit=treehit+1                      #내부값 갱신
#     print("파멸의 불꽃 데스나이트 전설의 울트라슈퍼킹갓재너럴슈퍼뿌슝레알레전더리탑오브더탑 그런트 나무 장로를 %d번 크리티컬로 후려 갈겼습니다." %treehit)
#     if treehit==999999:                         #세부적인 조건
#         print("마지막 최후의 일격을 파멸의 불꽃 데스나이트 전설의 울트라슈퍼킹갓재너럴슈퍼뿌슝레알레전더리탑오브더탑 그런트 나무 장로가 회피하였습니다.")
treehit=0
while treehit < 99:                         #조건
    treehit=treehit+1                      #내부값 갱신
    print("파일 다운로드가 %d"%" 진행되었습니다." %treehit)
    if treehit==99:                         #세부적인 조건
        print(".")





#while-break문 예시
# coffee = 10
# while True:
#     money=int(input("돈 내놔 : "))
#     if money==300:
#         print("커피를 뱉는다")
#         coffee -= 1
#     elif money > 300:
#         print("남는 돈 %d를 주고 커피를 뱉습니다. 그리고 다시 소매치기합니다." %(money-300))
#         coffee -= 1
#     else:
#         print("돈을 뺏고 커피를 주지 않습니다.")
#     print("남은 커피의 양은 %d다" %coffee)
#     if coffee== 0:
#         print("커피를 내가 다 마셨습니다. 내가 마실것도 부족해 77ㅓ억")
#         break


#while-continue
# a = 0
# while a < 10:
#     a = a+1
#     if a%2 == 0:
#         continue
#     print(a)