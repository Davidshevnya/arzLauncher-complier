<?php
list($host, $port) = explode(":", "185.169.134.43:7777"); // онярюбэре ябни юидх!!
$query = new Query($host, $port);
$query->connect();
$players = $query->getInformation()['players'];
$max_players = $query->getInformation()['max_players'];
$serverName = "Arizona TEST";
echo '{"arizona":[{"number":1,"name":"'.$serverName.'","ip":"'.$host.'","port":'.$port.',"online":'.$players.',"maxplayers":'.$max_players.',"password":false}]}';
?>