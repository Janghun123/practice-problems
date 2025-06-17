import pygame
import sys
import random

# 초기화
pygame.init()
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("파이썬 2D 게임")
clock = pygame.time.Clock()

# 플레이어 설정
player_size = 20
x, y = WIDTH // 2, HEIGHT - 50  # 아래쪽 시작 위치
speed = 10

# 색상 정의
WHITE = (160, 160, 160)
BLUE = (40, 40, 40)
RED = (200, 30, 30)
YELLOW = (250, 220, 50)

# 총알 설정
bullets = []  # 총알 리스트: 각 총알은 {'x': x좌표, 'y': y좌표}
bullet_speed = 10
bullet_limit = 10

# 적 설정
enemy_size = 40
enemy_speed = 4
enemies = []

def spawn_enemy():
    # 화면 상단에 랜덤한 위치에서 적 생성
    ex = random.randint(0, WIDTH - enemy_size)
    ey = -enemy_size
    enemies.append({'x': ex, 'y': ey})

# 충돌 판정 함수
def is_collision(a, b, size):
    return (a['x'] < b['x'] + size and a['x'] + size > b['x'] and
            a['y'] < b['y'] + size and a['y'] + size > b['y'])

# 게임 루프
running = True
frame_count = 0

while running:
    clock.tick(120)  # 초당 120프레임
    frame_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 마우스 좌클릭 시 총알 발사 (남은 총알 있을 때만)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if bullet_limit > 0:
                bullets.append({'x': x + player_size // 2 - 2, 'y': y})
                bullet_limit -= 1

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: x -= speed
    if keys[pygame.K_d]: x += speed
    if keys[pygame.K_w]: y -= speed
    if keys[pygame.K_s]: y += speed

    # 화면 경계 제한
    x = max(0, min(x, WIDTH - player_size))
    y = max(0, min(y, HEIGHT - player_size))

    # 적 주기적으로 생성
    if frame_count % 60 == 0:
        spawn_enemy()

    # 총알 이동
    for bullet in bullets:
        bullet['y'] -= bullet_speed
    bullets = [b for b in bullets if b['y'] > 0]  # 화면 밖 총알 제거

    # 적 이동
    for enemy in enemies:
        enemy['y'] += enemy_speed
    enemies = [e for e in enemies if e['y'] < HEIGHT]  # 화면 밖 적 제거

    # 충돌 판정 (총알 vs 적)
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if is_collision(bullet, enemy, enemy_size):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # 화면 그리기
    screen.fill(WHITE)

    # 플레이어 그리기
    pygame.draw.rect(screen, BLUE, (x, y, player_size, player_size))

    # 총알 그리기
    for bullet in bullets:
        pygame.draw.rect(screen, YELLOW, (bullet['x'], bullet['y'], 4, 10))

    # 적 그리기
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy['x'], enemy['y'], enemy_size, enemy_size))

    # 남은 총알 수 표시
    font = pygame.font.SysFont(None, 24)
    ammo_text = font.render(f"Ammo: {bullet_limit}", True, (0, 0, 0))
    screen.blit(ammo_text, (10, 10))

    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
