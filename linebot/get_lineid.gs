// line developersに書いてあるChannel Access Token
var access_token = "ojt*******************************************"
// pushしたいときに送る先のuser_id or group_idを指定する
var to = "U7*******************************"
// postされたログを残すスプレッドシートのid
var spreadsheet_id = "1rL**************************"

/**
 * 指定のuser_idにpushをする
 */
function push(text) {
  var url = "https://api.line.me/v2/bot/message/push";
  var headers = {
    "Content-Type" : "application/json; charset=UTF-8",
    'Authorization': 'Bearer ' + access_token,
  };

  var postData = {
    "to" : to,
    "messages" : [
      {
        'type':'text',
        'text':text,
      }
    ]
  };

  var options = {
    "method" : "post",
    "headers" : headers,
    "payload" : JSON.stringify(postData)
  };

  return UrlFetchApp.fetch(url, options);
}

/**
 * reply_tokenを使ってreplyする
 */
function reply(data) {
  var url = "https://api.line.me/v2/bot/message/reply";
  var headers = {
    "Content-Type" : "application/json; charset=UTF-8",
    'Authorization': 'Bearer ' + access_token,
  };

  var postData = {
    "replyToken" : data.events[0].replyToken,
    "messages" : [
      {
        'type':'text',
        'text':data.events[0].message.text + 'ぱち',
      }
    ]
  };

  var options = {
    "method" : "post",
    "headers" : headers,
    "payload" : JSON.stringify(postData)
  };

  return UrlFetchApp.fetch(url, options);
}

/**
 * postされたときの処理
 */
function doPost(e) {
  var json = JSON.parse(e.postData.contents);
  var data = SpreadsheetApp.openById(spreadsheet_id).getSheetByName('log').getRange(1, 1).setValue(json.events);

  reply(json);
}

/**
 * pushをしてみる
 */
function test() {
  push('ぱちぱち');
}
