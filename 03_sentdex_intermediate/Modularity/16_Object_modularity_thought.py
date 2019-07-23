# 13_Object_oriented_programming_intro
# 14_Creating_an_environment_intro
# 15_Many_blob_object
# 16 Object Modularity Thoughts

import pygame
from blob import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob world")
clock = pygame.time.Clock()


def draw_environment(blob_list):
    game_display.fill(WHITE)

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            if blob.x < 0: blob.x = 0
            elif blob.x > blob.x_boundary: blob.x = blob.x_boundary
            if blob.y < 0: blob.y = 0
            elif blob.y > blob.y_boundary: blob.y = blob.y_boundary
    pygame.display.update()


def main():
    blue_blobs = dict(enumerate([Blob(BLUE,WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([Blob(RED,WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    print(blue_blobs)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs, red_blobs])
        clock.tick(60)


if __name__ == "__main__":
    main()
