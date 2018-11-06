module.exports = {
  'home test' : function (client) {
    client
      .url('https://s3-ap-northeast-1.amazonaws.com/peter-test-stage-gcp/file-send-test/trynightwatch/index.html')
      .pause(1000)
      .waitForElementVisible('body', 1000)
      .assert.title('whoaaa')
      .assert.visible("p#samurai")
      .waitForElementVisible('#yay', 1000)
      .assert.containsText("#yay", "yay")
      .end()
  }
}
