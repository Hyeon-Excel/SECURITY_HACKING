import socket # 네트워크 통신을 위한 라이브러리

target_host = "google.com" # 스캔할 목표
ports_to_scan = [80, 443, 8080] # 스캔할 포트 목록

print(f"[*] {target_host}에 대한 포트 스캔을 시작합니다...")

# ports_to_scan 목록의 각 포트에 대해 반복
for port in ports_to_scan:
    try:
        # 소켓 객체를 생성하고 타임아웃을 1초로 설정
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # 지정된 호스트와 포트로 연결을 시도
        result = sock.connect_ex((target_host, port))
        
        # 연결에 성공하면(결과가 0이면) 포트가 열려있다는 의미
        if result == 0:
            print(f"  [+] 포트 {port} 열려있음")
        # else: # 닫혀있는 포트는 출력하지 않음
        #     print(f"  [-] 포트 {port} 닫혀있음")
            
        sock.close() # 소켓을 닫음

    except socket.error as e:
        print(f"소켓 에러 발생: {e}")

print("[*] 포트 스캔 완료.")