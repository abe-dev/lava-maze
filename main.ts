scene.onOverlapTile(SpriteKind.Player, sprites.builtin.field0, function (sprite, location) {
    game.over(true)
})
let mySprite = sprites.create(assets.image`Char_Robert`, SpriteKind.Player)
controller.moveSprite(mySprite)
tiles.setTilemap(tilemap`level1`)
tiles.placeOnRandomTile(mySprite, sprites.builtin.field1)
scene.cameraFollowSprite(mySprite)
info.startCountdown(10)
