<?php
/**
 *
 *  ____  _   _ ____    ____    _         __  __ ____
 * |  _ \| | | |  _ \  / ___|  / \       |  \/  |  _ \
 * | |_) | |_| | |_) | \___ \ / _ \ _____| |\/| | |_) |
 * |  __/|  _  |  __/   ___) / ___ \_____| |  | |  __/
 * |_|   |_| |_|_|     |____/_/   \_\    |_|  |_|_|
 *
 * This project is not affiliated with SA-MP team nor RakNet.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * @Author: xISRAPILx
 */

class Query{

    /** @var string */
    private $address;

    /** @var int */
    private $port;

    /** @var resource */
    private $socket;

    /**
     * Query constructor.
     *
     * @param string $address
     * @param int    $port
     */
    public function __construct(string $address, int $port){
        $this->address = $address;
        $this->port = $port;
    }

    public function __destruct(){
        fclose($this->socket);
    }

    /**
     * @return bool
     * @throws QueryException
     */
    public function connect() : bool{
        if(is_resource($this->socket))
            fclose($this->socket);
        
        $this->socket = fsockopen("udp://".$this->address, $this->port, $error_id, $error, 4);

        if(!$this->socket)
            throw new QueryException("Ошибка подключение к серверу!".PHP_EOL."[".$error_id."] ".$error);

        return $this->socket === false ? false : true;
    }

    /**
     * Получение базовой информации с сервера(Онлайн, название, игроковой режим и тд.).
     *
     * @return array|null
     * @throws QueryException
     */
    public function getInformation() : ?array{
        if(!is_resource($this->socket)){
            throw new QueryException("Невозможно вызвать данный метод не инициализировав соккет.");
        }

        if(!fwrite($this->socket, $this->createBasePacket("i"))){
            throw new QueryException("Ошибка записи пакета в соккет. ".@socket_last_error($this->socket));
        }

        if(!fread($this->socket, 11)){
            throw new QueryException("Ошибка чтения пакета из сокет. ".@socket_last_error($this->socket));
        }

        $information["password"] = (bool) Binary::readByte(fread($this->socket, 1)); //Статус пароля сервера
        $information["players"] = Binary::readLShort(fread($this->socket, 2)); //Кол-во игроков онлайн
        $information["max_players"] = Binary::readLShort(fread($this->socket, 2)); //Максимальное количество игроков.
        $information["hostname"] = Binary::readLInt(fread($this->socket, 4)); //Длина названия сервера
        $information["hostname"] = fread($this->socket, $information["hostname"]); //Само название сервера
        $information["gamemode"] = Binary::readLInt(fread($this->socket, 4)); //Длина игрового режима сервера
        $information["gamemode"] = fread($this->socket, $information["gamemode"]); //Сам игроков режим сервера
        $information["language"] = Binary::readLInt(fread($this->socket, 4)); //Длина языка сервера
        $information["language"] = fread($this->socket, $information["language"]); //Сам язык сервера

        return $information;
    }

    /**
     * Получение всех правил(параметров) сервера.
     *
     * @return array|null
     * @throws QueryException
     */
    public function getRules() : ?array{
        if(!is_resource($this->socket)){
            throw new QueryException("Невозможно вызвать данный метод не инициализировав соккет.");
        }

        if(!fwrite($this->socket, $this->createBasePacket("r"))){
            throw new QueryException("Ошибка записи пакета в соккет. ".@socket_last_error($this->socket));
        }

        if(!fread($this->socket, 11)){
            throw new QueryException("Ошибка чтения пакета из сокет. ".@socket_last_error($this->socket));
        }

        $rules["count"] = Binary::readLShort(fread($this->socket, 2));
        for($i = 0; $i < $rules["count"]; ++$i){
            $name = fread($this->socket, Binary::readByte(fread($this->socket, 1)));
            $value = fread($this->socket, Binary::readByte(fread($this->socket, 1)));

            $rules["rules"][$name] = $value;
        }

        return $rules;
    }

    /**
     * Получение игроков сервера.
     *
     * @return array|null
     * @throws QueryException
     */
    public function getClients() : ?array{
        if(!is_resource($this->socket)){
            throw new QueryException("Невозможно вызвать данный метод не инициализировав соккет.");
        }

        if(!fwrite($this->socket, $this->createBasePacket("c"))){
            throw new QueryException("Ошибка записи пакета в соккет. ".@socket_last_error($this->socket));
        }

        if(!fread($this->socket, 11)){
            throw new QueryException("Ошибка чтения пакета из сокет. ".@socket_last_error($this->socket));
        }

        $clients["count"] = Binary::readLShort(fread($this->socket, 2));
        for($i = 0; $i < $clients["count"]; ++$i){
            $nickname = fread($this->socket, Binary::readByte(fread($this->socket, 1)));
            $score = Binary::readLInt(fread($this->socket, 4));

            $clients["clients"][$nickname] = $score;
        }

        return $clients;
    }

    /**
     * Получение дополнительной информации об игроках
     *
     * @return array|null
     * @throws QueryException
     */
    public function getClientsDetailed() : ?array{
        if(!is_resource($this->socket)){
            throw new QueryException("Невозможно вызвать данный метод не инициализировав соккет.");
        }

        if(!fwrite($this->socket, $this->createBasePacket("d"))){
            throw new QueryException("Ошибка записи пакета в соккет. ".@socket_last_error($this->socket));
        }

        if(!fread($this->socket, 11)){
            throw new QueryException("Ошибка чтения пакета из сокет. ".@socket_last_error($this->socket));
        }

        $clients["count"] = Binary::readLShort(fread($this->socket, 2));
        for($i = 0; $i < $clients["count"]; ++$i){
            $player_id = Binary::readByte(fread($this->socket, 1));
            $nickname = fread($this->socket, Binary::readByte(fread($this->socket, 1)));
            $score = Binary::readLInt(fread($this->socket, 4));
            $ping = Binary::readLInt(fread($this->socket, 4));

            $clients["clients"][$nickname] = ["id" => $player_id, "score" => $score, "ping" => $ping];
        }

        return $clients;
    }

    /**
     * @param string $opcode
     *
     * @return string
     */
    public function createBasePacket(string $opcode = "i") : string{
        $address = explode(".", $this->address);

        $packet = "SAMP";
        $packet .= Binary::writeByte($address[0]);
        $packet .= Binary::writeByte($address[1]);
        $packet .= Binary::writeByte($address[2]);
        $packet .= Binary::writeByte($address[3]);
        $packet .= Binary::writeLShort($this->port);
        $packet .= $opcode;

        return $packet;
    }

    /**
     * @return string
     */
    public function getAddress() : string{
        return $this->address;
    }

    /**
     * @param string $address
     */
    public function setAddress(string $address) : void{
        $this->address = $address;
    }

    /**
     * @return int
     */
    public function getPort() : int{
        return $this->port;
    }

    /**
     * @param int $port
     */
    public function setPort(int $port) : void{
        $this->port = $port;
    }
}

class Binary{

    /**
     * @param string $value
     *
     * @return int
     */
    public static function readByte(string $value) : int{
        return ord($value{0});
    }

    /**
     * @param int $value
     *
     * @return string
     */
    public static function writeByte(int $value) : string{
        return chr($value);
    }

    /**
     * @param string $value
     *
     * @return int
     */
    public static function readLShort(string $value) : int{
        return unpack("v", $value)[1];
    }

    /**
     * @param int $value
     *
     * @return string
     */
    public static function writeLShort(int $value) : string{
        return pack("v", $value);
    }

    /**
     * @param string $value
     *
     * @return int
     */
    public static function readLInt(string $value) : int{
        return unpack("V", $value)[1] << 32 >> 32;
    }

    /**
     * @param int $value
     *
     * @return string
     */
    public static function writeLInt(int $value) : string{
        return pack("V", $value);
    }
}

class QueryException extends \Exception{}