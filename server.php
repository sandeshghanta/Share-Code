<?php
	if (isset($_GET['filename']) && isset($_GET['password'])){
		$host = "fdb14.biz.nf";
		$username = "2261537_data";
		$password = "sandeshghanta047";
		$link = mysqli_connect($host, $username, $password);
		mysqli_select_db($link,"2261537_data");
		$filename = substr(str_shuffle(str_repeat("0123456789abcdefghijklmnopqrstuvwxyz", 5)), 0, 5);
		$command = "select * from data where savedname ='".$filename."';";
		while (mysqli_num_rows(mysqli_query($link,$command)) != 0){
			$filename = substr(str_shuffle(str_repeat("0123456789abcdefghijklmnopqrstuvwxyz", 5)), 0, 5);
			$command = "select * from data where savedname ='".$filename."';";
		}
		$command = "insert into data (filename,savedname,password) values ('" . $_GET['filename'] . "','" . $filename . "','" . $_GET['password'] . "');";
		$result = mysqli_query($link,$command);
		if ($result){
			move_uploaded_file($_FILES["file"]["tmp_name"],'files/'.$filename);
			echo "File Uploaded Successfully\n"
			echo "Command to get your file 'get.py ".$filename."'\n";
			echo "Or you can go to 'sharecode.co.nf/".$filename."'\n";
		}
		else{
			echo "Some error occured please try again\n";
		}
	}
	else{
		echo "False";
	}
?>