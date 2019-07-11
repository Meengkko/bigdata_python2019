import sys
sys.path.append('.')
# import game.sound.echo
# game.sound.echo.echo_test()

# from game.sound import echo
# echo.echo_test()

# from game.sound.echo import echo_test
# echo_test()

# 만약에 sound, play 패키지 안에 모두 echo 모듈이 있고 아래와 같이 동일한
# 함수가 있다면 모듈, 함수()로 구별아혀 호출해야 한다.
# from game.sound.echo import *
# echo_test()

from new_pkg.game.sound import *
from new_pkg.game.graphic import *
echo.echo_test()
wave.wave_test()
render.render_test()
