idea 적자

```mermaid
graph TD;
    RFID-찍기 --> 읽기 --> 초기화 --> request-보내기
    QR-인식 --> json-데이터-가져오기 --> request-보내기
    request-보내기 --> 누가,몇시,출석혹은보건실등등,과목
```