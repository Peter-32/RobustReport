var i = 1
function addQuery() {
  i = i + 1
  var str = `          <fieldset class="pure-group query`+i+`">
    <input type="text" class="pure-input-1-2" placeholder="A title" name="query`+i+`_name" value="test title">
    <textarea rows="12" class="pure-input-1-2" placeholder="Put SQL here" name="query`+i+`_sql">test SQL</textarea>
    <label for="visible_checkbox" class="pure-checkbox" id="visible_checkbox_label">
      Visible:</label>
      <input id="visible_checkbox" type="checkbox" value="" name="query`+i+`_visible_checkbox" checked>
      <div class="pure-u-1 pure-u-md-1-3">
        <label for="connection" id="connection_label">Connection:</label>
        <select id="connection" class="pure-input-1-2" name="query`+i+`_connection">
          <option>Inmemory</option>
          <option>Connection 1</option>
          <option>Connection 2</option>
          <option>Connection 3</option>
          <option>Connection 4</option>
          <option>Connection 5</option>
          <option>Connection 6</option>
          <option>Connection 7</option>
          <option>Connection 8</option>
        </select>
      </div>
    </fieldset>
    <div id="query`+(i+1)+`"></div>
    `
    document.getElementById("query"+i).innerHTML = str
    document.getElementById("query_count").value = i

    //alert(str)
}
