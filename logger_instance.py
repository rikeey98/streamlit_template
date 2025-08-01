# logger_instance.py
"""
전역 로거 인스턴스
모든 모듈에서 import해서 사용할 수 있는 로거
"""
import os
from logging_config import create_logger_with_config

# 설정 파일 경로
CONFIG_FILE = "logging_config.yaml"

# 전역 로거 인스턴스 생성
logger, decorators, monitor = create_logger_with_config(CONFIG_FILE)

# 선택사항: 환경 정보 출력
if __name__ != "__main__":  # import될 때만 출력
    config_info = logger.get_config_info()
    print(f"🔧 로거 초기화 완료: {config_info['environment']} 환경")
    print(f"📁 로그 디렉토리: {config_info['log_dir']}")

# 편의를 위한 별칭 (선택사항)
log = logger  # 짧은 이름으로 사용하고 싶을 때
