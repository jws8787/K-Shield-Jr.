어셈블리어
===============
범용 레지스터
-----
+ AX(16Bit), EAX(32Bit), RAX(64Bit)
    + 곱셈과 나눗셈 명령에서 자동으로 사용, 함수의 리턴값이 저장되는 용도
    + AH(8Bit) + AL(8Bit)
+ BX(16Bit), EBX(32Bit), RBX(64Bit)
    + ESI나 EDI와 결합하여 인덱스에 사용
        + ESI/SI : 소스 주소
        + EDI/DI : 목적지 주소
+ CX(16Bit), ECX(32Bit), RCX(64Bit)
    + 반복 명령어 사용시 반복 카운터로 사용
+ DX(16Bit), EDX(32Bit), RDX(64Bit)
    + AX와 같이 쓰이며 부호 확장 명령 등에 사용
