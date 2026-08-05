<?php
/* Makes sure that image and file uploads have lowercase filenames.

This is a sample snippet. Feel free to use it, edit it, or remove it. */
add_filter( 'sanitize_file_name', 'mb_strtolower' );