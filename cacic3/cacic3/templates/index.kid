<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" py:replace="''"/>
    <title>CACIC3</title>
</head>
<body>
    <div id="computers">
        <div py:for="computer in computers" id="computer_${computer.te_node_address}">
            <h2 py:content="computer.te_nome_computador">Computer Name here</h2>
            <div class="computermeta">
            </div>
        </div>
    </div>
</body>
</html>
