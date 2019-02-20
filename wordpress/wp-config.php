<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'mylinh');

/** MySQL database password */
define('DB_PASSWORD', '12345678');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'u.:{{nl#)@0tz?G}?q0@=?VXUXdC<C)cHZdc$_L%^Sfih=w76iG I6dNC&=TMeQ;');
define('SECURE_AUTH_KEY',  'Ow?Wk2g*rlmO{ r(9XYC_h[bykw!* R/[qw-!x+E<)3l*ecgI56z9 e?g|2K&{@9');
define('LOGGED_IN_KEY',    'XM~.wt+]x2$SgH?$k(nl&XCrNAVB]%_|rUxR/O.D1/)s@([K9U?|pc&O9,[UZVNx');
define('NONCE_KEY',        '45ejQnL|h.|)|r NY Twb#889[iH+_:uPH<%R HvX/]_N]dwu/-pFqoBgvOMF%8)');
define('AUTH_SALT',        'q^=6~KrnUh1x+>.K,b_Rg=$%9Z6iU-5aY?u%IxFJSTFT~_-HK-Z_Rk0UR{Vpw++h');
define('SECURE_AUTH_SALT', ';mXmahG;X(VWez`pTbUUqxYM3CQ&h58pmQ{]BQ{UyRW(EGwd(IbKvgVb`6:SjqVy');
define('LOGGED_IN_SALT',   '+x&.*`uU.Xi]et!svQdk:%5p4kwVa?<Wl4/|J,w`:zkIYhj|jgaokwb{Su Br%=`');
define('NONCE_SALT',       'lY-?1Xf=kW8C|mpE I&k2LJtNfM z NZ4*oE&l6n$dmx*-sguQ MGy0o+yw7b{F@');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
