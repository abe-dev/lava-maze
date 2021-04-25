def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player, sprites.builtin.field0, on_overlap_tile)

mySprite = sprites.create(assets.image("""
    Char_Robert
"""), SpriteKind.player)
controller.move_sprite(mySprite)
tiles.set_tilemap(tilemap("""
    level1
"""))
tiles.place_on_random_tile(mySprite, sprites.builtin.field1)
scene.camera_follow_sprite(mySprite)
info.start_countdown(10)