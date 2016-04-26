# 시저 암호
****
### 설명
시저암호(CaesarCipher)는 입력받은 문자열을 key값에 따라 암호화하는 알고리즘이다. 입력받는 key값은 정수 값으로 key 값만큼 각각의 문자를 이동하도록 하여 입력받은 문자열을 알아보기 어려운 암호문으로 만들어낸다. 예를 들어, 입력받은 문자열이 **hello**이고 key 값이 **3**일 때, **hello**의 시저암호문은 각 문자를 알파벳 순으로 **3**만큼 이동시킨 **khoor**이다.

### 주의할 점
- 오직 알파벳(대문자와 소문자)만 이동해야 합니다.
- 예를 들어, **y**를 **1**만큼 이동시키면 **z**, **2**만큼 이동시키면 **a**, **3**만큼 이동시키면 **b**입니다.

### 예제 1
![](/week07/p1/00.png)

### 예제 2
![](/week07/p1/01.png)