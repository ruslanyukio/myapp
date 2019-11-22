


$('#menu_btn').click(() => {

	$('#main_datas_block').css({
		'height': 'auto',
		'display': 'block',
		'padding': '30px 30px 15px 30px',
		'transition': '0.5s ease',
	});

	$('#main_datas_block div').css({
		'display': 'block',
	});

	$('#main_datas_block h2').css({
		'display': 'block',
	});
});

var aply = false

$('#data_user button').click(() => {
	if (aply == false){
			$('#data_user button img').css({
				'transform': 'scale(1, -1)',
				'-o-transform': 'scale(1, -1)',
				'-moz-transform': 'scale(1, -1)',
				'-webkit-transform': 'scale(1, -1)',
				'transition': '0.3s ease',
				'-o-transition': '0.3s ease',
				'-moz-transition': '0.3s ease',
				'-webkit-transition': '0.3s ease',
			});

				$('#main_datas_block').css({
					'height': 'auto',
					'display': 'block',
					'padding': '30px 30px 15px 30px',
					'transition': '0.5s ease',
					'-o-transition': '0.5s ease',
					'-moz-transition': '0.5s ease',
					'-webkit-transition': '0.5s ease',
				});

				$('#main_datas_block div').css({
					'display': 'block',
				});
				$('#childs').css({
				'display': 'flex',
				'justify-content': 'flex-start',
			});

				$('#main_datas_block h2').css({
					'display': 'block',
				});
			aply = true;
	} else {
		$('#childs').css({
				'display': 'none'
			});
		$('#data_user button img').css({
				'transform': 'scale(-1, 1)',
				'-o-transform': 'scale(-1, 1)',
				'-moz-transform': 'scale(-1, 1)',
				'-webkit-transform': 'scale(-1, 1)',
				'transition': '0.3s ease',
				'-o-transition': '0.3s ease',
				'-moz-transition': '0.3s ease',
				'-webkit-transition': '0.3s ease',
			});

			$('#main_datas_block').css({
				'height': '0px',
				'display': 'block',
				'padding': '0',
				'transition': '0.5s ease',
				'-o-transition': '0.5s ease',
				'-moz-transition': '0.5s ease',
				'-webkit-transition': '0.5s ease',
			});

			$('#main_datas_block div').css({
				'display': 'none',
			});

			$('#main_datas_block h2').css({
				'display': 'none',
			});
		aply = false;
	}
});

