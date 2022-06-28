#환경변수 확인 : window - set / mac - env

#key = values 형태

#활용이유
# 복잡한 코드들의 집합 중 변경사항 손쉽게 설정
# API KEY 등 코드와 분리하여 저장 필요 - 특히, 결제정보 등 연결되어 있는 경우

#환경변수 설정방법
# console 화면 > export 환경변수 설정 key 값=value 값 (단, space 없이)
# 해당 코드 변경 : os.environ.get("key")

'''
GROUPS=()
HISTCONTROL=ignoreboth
HISTFILE=/home/HyeryunKim/.bash_history
HISTFILESIZE=500
HISTSIZE=500
HOME=/home/HyeryunKim
HOSTNAME=green-liveconsole21
HOSTTYPE=x86_64
IFS=$' \t\n'
JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
LC_CTYPE=en_US.utf-8
LIGHT_GRAY='\[\033[0;37m\]'
LIGHT_GREEN='\[\033[1;32m\]'
LINES=22
LOGNAME=HyeryunKim
MACHTYPE=x86_64-pc-linux-gnu
MAILCHECK=60
OLDPWD=/home/HyeryunKim
OPTERR=1
OPTIND=1
OSTYPE=linux-gnu
PATH=/home/HyeryunKim/.local/bin:/usr/local/julia-1.6.1/bin:/home/HyeryunKim/.local/bin:/usr/local/julia-1.6.1/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PIPESTATUS=([0]="1")
PPID=0
PS1='\[\033[0;37m\]$(date +%H:%M) \w\[\033[0;33m\] $(parse_git_branch)\[\033[1;32m\]$ \[\033[0;37m\]'
PS2='> '
PS4='+ '
PWD=/home/
'''