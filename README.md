<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Esp → Discord bot token by PYTHON</title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	padding-inline-start: 0;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

.page-description {
	margin-bottom: 2em;
}

.simple-table {
	margin-top: 1em;
	font-size: 0.875rem;
	empty-cells: show;
}
.simple-table td {
	height: 29px;
	min-width: 120px;
}

.simple-table th {
	height: 29px;
	min-width: 120px;
}

.simple-table-header-color {
	background: rgb(247, 246, 243);
	color: black;
}
.simple-table-header {
	font-weight: 500;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	max-height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(50, 48, 44, 1);
}
.highlight-gray {
	color: rgba(115, 114, 110, 1);
	fill: rgba(115, 114, 110, 1);
}
.highlight-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.highlight-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.highlight-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.highlight-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.highlight-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.highlight-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.highlight-red {
	color: rgba(205, 60, 58, 1);
	fill: rgba(205, 60, 58, 1);
}
.highlight-default_background {
	color: rgba(50, 48, 44, 1);
}
.highlight-gray_background {
	background: rgba(248, 248, 247, 1);
}
.highlight-brown_background {
	background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
	background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.highlight-teal_background {
	background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
	background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
	background: rgba(248, 243, 252, 1);
}
.highlight-pink_background {
	background: rgba(252, 241, 246, 1);
}
.highlight-red_background {
	background: rgba(253, 235, 236, 1);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(115, 114, 110, 1);
	fill: rgba(115, 114, 110, 1);
}
.block-color-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.block-color-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.block-color-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.block-color-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.block-color-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.block-color-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.block-color-red {
	color: rgba(205, 60, 58, 1);
	fill: rgba(205, 60, 58, 1);
}
.block-color-default_background {
	color: inherit;
	fill: inherit;
}
.block-color-gray_background {
	background: rgba(248, 248, 247, 1);
}
.block-color-brown_background {
	background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
	background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.block-color-teal_background {
	background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
	background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
	background: rgba(248, 243, 252, 1);
}
.block-color-pink_background {
	background: rgba(252, 241, 246, 1);
}
.block-color-red_background {
	background: rgba(253, 235, 236, 1);
}
.select-value-color-default { background-color: rgba(84, 72, 49, 0.08); }
.select-value-color-gray { background-color: rgba(84, 72, 49, 0.15); }
.select-value-color-brown { background-color: rgba(210, 162, 141, 0.35); }
.select-value-color-orange { background-color: rgba(224, 124, 57, 0.27); }
.select-value-color-yellow { background-color: rgba(236, 191, 66, 0.39); }
.select-value-color-green { background-color: rgba(123, 183, 129, 0.27); }
.select-value-color-blue { background-color: rgba(93, 165, 206, 0.27); }
.select-value-color-purple { background-color: rgba(168, 129, 197, 0.27); }
.select-value-color-pink { background-color: rgba(225, 136, 179, 0.27); }
.select-value-color-red { background-color: rgba(244, 171, 159, 0.4); }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="7b3444b6-8402-4dae-bc01-2670be97810c" class="page sans"><header><img class="page-cover-image" src="https://images.unsplash.com/photo-1553341640-9397992456f3?ixlib=rb-4.0.3&amp;q=85&amp;fm=jpg&amp;crop=entropy&amp;cs=srgb" style="object-position:center 50%"/><h1 class="page-title">Esp → Discord bot token by PYTHON</h1><p class="page-description"></p></header><div class="page-body"><p id="62f371c8-23ce-494f-bd21-f12550e763a1" class="">การสร้าง Token discord</p><figure id="10910dc0-8ab0-80f2-b8e3-eaed5fdc579d" class="link-to-page"><a href="https://www.notion.so/Generate-Discord-Bot-Token-Use-It-10910dc08ab080f2b8e3eaed5fdc579d?pvs=21">Generate Discord Bot Token &amp; Use It</a></figure><div id="10910dc0-8ab0-80db-bcf9-d640eaaa8d4b" class="column-list"><div id="a7faffed-8066-472a-84a7-bc1b94d62353" style="width:50.000000000000014%" class="column"><figure id="10910dc0-8ab0-8091-95c9-c046c701ecf2" class="image" style="text-align:center"><a href="1._RFID__(1).png"><img style="width:720px" src="1._RFID__(1).png"/></a></figure></div><div id="10910dc0-8ab0-80f5-accc-c464ea4820a4" style="width:50%" class="column"><figure id="10910dc0-8ab0-805b-a215-e9c1f0d2adb8" class="image"><a href="1._RFID__(2).png"><img style="width:517.4000244140625px" src="1._RFID__(2).png"/></a></figure></div></div><div id="10910dc0-8ab0-803e-9840-f5db65b5cd90" class="column-list"><div id="6097fb10-fdec-40f4-94a8-3ae852644596" style="width:50%" class="column"><h2 id="5321463e-82b2-44c9-8c00-ed332d0af7ea" class=""><mark class="highlight-orange">Arduino code</mark></h2><h3 id="10910dc0-8ab0-80e8-946b-d8688529cc88" class="">1.การกำหนดค่าเบื้องต้น</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-809b-9a00-e7a44002b93b" class="code"><code class="language-C">#include &lt;WiFi.h&gt;
#include &lt;HTTPClient.h&gt;
#include &quot;DHT.h&quot;

#define DHTPIN 2  // กำหนดขาให้กับ DHT
#define DHTTYPE DHT22  // ใช้ DHT22 หรือ DHT11
DHT dht(DHTPIN, DHTTYPE);</code></pre><ul id="10910dc0-8ab0-80ac-8eb7-c5b5c27308a0" class="bulleted-list"><li style="list-style-type:disc"><code><strong>#define DHTPIN</strong></code>: กำหนดพอร์ตที่เชื่อมต่อกับเซ็นเซอร์ DHT (ขา GPIO 2 ในที่นี้)</li></ul><ul id="10910dc0-8ab0-80a5-b6fd-fb4cbfb91f49" class="bulleted-list"><li style="list-style-type:disc"><code><strong>#include</strong></code>: โหลดไลบรารีที่จำเป็นสำหรับการเชื่อมต่อ WiFi, การส่งข้อมูลผ่าน HTTP และการอ่านค่าเซ็นเซอร์ DHT</li></ul><ul id="10910dc0-8ab0-8036-86aa-c6876a0672e1" class="bulleted-list"><li style="list-style-type:disc"><code><strong>#define DHTTYPE</strong></code>: ระบุประเภทเซ็นเซอร์ DHT ที่ใช้ (DHT22 ในตัวอย่างนี้)</li></ul><h3 id="3bf44a56-c46f-41ff-9a54-a44e89a1c656" class="">2.การกำหนด WiFi และเซิร์ฟเวอร์</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-8016-9794-c40658687583" class="code"><code class="language-C">const char* ssid = &quot;Saranphat&quot;; // ใส่ชื่อ WiFi ของคุณ
const char* password = &quot;123456789&quot;; // ใส่รหัสผ่าน WiFi ของคุณ\
String serverIP = &quot;172.20.10.7&quot;; // ที่อยู่ local IP ของเซิร์ฟเวอร์ Python</code></pre><ul id="10910dc0-8ab0-8023-9b3d-c69ca33eb418" class="bulleted-list"><li style="list-style-type:disc"><code><strong>ssid</strong></code><strong> และ </strong><code><strong>password</strong></code>: ชื่อและรหัสผ่านของเครือข่าย WiFi ที่ต้องการเชื่อมต่อ</li></ul><ul id="10910dc0-8ab0-808a-9ab3-f6db0e8e520a" class="bulleted-list"><li style="list-style-type:disc"><code><strong>serverIP</strong></code>: ที่อยู่ IP ของเซิร์ฟเวอร์ Python ที่ ESP32 จะส่งข้อมูลไปให้</li></ul><h3 id="10910dc0-8ab0-8054-8be1-de91eded2604" class="">3.การตั้งค่าการเชื่อมต่อ</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-80d7-b45f-dc5040b5f555" class="code"><code class="language-C++" style="white-space:pre-wrap;word-break:break-all"> 
void setup() {
  Serial.begin(115200);
  dht.begin();
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println(&quot;Connecting to WiFi...&quot;);
  }

  Serial.println(&quot;WiFi connected.&quot;);
  Serial.print(&quot;ESP32 IP address: &quot;);
  Serial.println(WiFi.localIP());  // แสดง IP Address ของ ESP32 ที่เชื่อมต่อ
}

</code></pre><ul id="10910dc0-8ab0-80c5-89ca-d949b4288d57" class="bulleted-list"><li style="list-style-type:disc"><code><strong>Serial.begin(115200)</strong></code>: เปิดการสื่อสารผ่าน Serial Monitor เพื่อดูข้อมูลสถานะการเชื่อมต่อ</li></ul><ul id="10910dc0-8ab0-806d-b56a-faa515b2fb6d" class="bulleted-list"><li style="list-style-type:disc"><code><strong>WiFi.begin()</strong></code>: เชื่อมต่อ WiFi ด้วย SSID และรหัสผ่านที่ระบุ</li></ul><ul id="10910dc0-8ab0-8022-bb55-cb1ce8110542" class="bulleted-list"><li style="list-style-type:disc"><code><strong>while (WiFi.status() != WL_CONNECTED)</strong></code>: รอจนกว่า WiFi จะเชื่อมต่อสำเร็จ</li></ul><ul id="10910dc0-8ab0-8089-b692-fa740f1a19a6" class="bulleted-list"><li style="list-style-type:disc"><code><strong>WiFi.localIP()</strong></code>: แสดง IP Address ของ ESP32 ที่ได้รับจากเครือข่าย WiFi</li></ul><h3 id="7593c8ef-10ea-4309-9456-07b83148c9f0" class="">4.การอ่านค่า DHT และส่งข้อมูลไปยังเซิร์ฟเวอร์</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-8062-ac0e-d14ec4ce238c" class="code"><code class="language-C++" style="white-space:pre-wrap;word-break:break-all">
void loop() {
  float temp = dht.readTemperature();
  float humid = dht.readHumidity();

  if (isnan(temp) || isnan(humid)) {
    Serial.println(&quot;Failed to read from DHT sensor!&quot;);
    return;
  }

  // แสดงค่าอุณหภูมิและความชื้น
  Serial.print(&quot;Temperature: &quot;);
  Serial.print(temp);
  Serial.println(&quot;°C&quot;);
  Serial.print(&quot;Humidity: &quot;);
  Serial.print(humid);
  Serial.println(&quot;%&quot;);

</code></pre><ul id="10910dc0-8ab0-80e5-9b15-f7cecc89134e" class="bulleted-list"><li style="list-style-type:disc"><code><strong>dht.readTemperature()</strong></code><strong> และ </strong><code><strong>dht.readHumidity()</strong></code>: อ่านค่าอุณหภูมิและความชื้นจากเซ็นเซอร์ DHT</li></ul><ul id="10910dc0-8ab0-80a9-a78b-e7a318a82970" class="bulleted-list"><li style="list-style-type:disc"><code><strong>isnan()</strong></code>: ตรวจสอบว่าการอ่านค่าจากเซ็นเซอร์เป็นไปอย่างถูกต้องหรือไม่</li></ul><ul id="10910dc0-8ab0-80c6-915c-f641c55e11dc" class="bulleted-list"><li style="list-style-type:disc"><code><strong>Serial.print()</strong></code>: แสดงผลค่าอุณหภูมิและความชื้นใน Serial Monitor</li></ul><h3 id="10910dc0-8ab0-8093-a697-de001bb912d1" class="">5.การส่งข้อมูลผ่าน HTTP</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-8084-acf1-f46e529c011c" class="code"><code class="language-C++" style="white-space:pre-wrap;word-break:break-all">cpp
Copy code
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    String serverURL = &quot;http://&quot; + serverIP + &quot;:5000/update&quot;;
    http.begin(serverURL);

    http.addHeader(&quot;Content-Type&quot;, &quot;application/json&quot;);
    String jsonData = &quot;{\&quot;temp\&quot;: &quot; + String(temp) + &quot;, \&quot;humid\&quot;: &quot; + String(humid) + &quot;}&quot;;

    int httpResponseCode = http.POST(jsonData);
    Serial.print(&quot;HTTP Response code: &quot;);
    Serial.println(httpResponseCode);
    http.end();
  }

  delay(10000); // อัปเดตทุกๆ 10 วินาที (ปรับเปลี่ยนตามที่คุณต้องการ)
}</code></pre><ul id="b81b3814-2cce-4421-8951-8b18c22c9dfc" class="bulleted-list"><li style="list-style-type:disc"><code><strong>WiFi.status() == WL_CONNECTED</strong></code>: ตรวจสอบว่า ESP32 ยังคงเชื่อมต่อกับ WiFi อยู่หรือไม่</li></ul><ul id="10910dc0-8ab0-8018-ad74-e50a1bcb22c9" class="bulleted-list"><li style="list-style-type:disc"><code><strong>HTTPClient http</strong></code>: สร้าง HTTP Client เพื่อส่งข้อมูล</li></ul><ul id="d6ba22b1-1f4e-4697-b9c0-e452ba8463e7" class="bulleted-list"><li style="list-style-type:disc"><code><strong>http.begin()</strong></code>: เริ่มต้นเชื่อมต่อกับ URL ของเซิร์ฟเวอร์ Python</li></ul><ul id="10910dc0-8ab0-8043-b9b8-d7236415713a" class="bulleted-list"><li style="list-style-type:disc"><code><strong>http.addHeader(&quot;Content-Type&quot;, &quot;application/json&quot;)</strong></code>: กำหนดประเภทข้อมูลที่ส่ง (เป็น JSON)</li></ul><ul id="10910dc0-8ab0-808b-8b99-fe95bb9d1201" class="bulleted-list"><li style="list-style-type:disc"><code><strong>http.POST(jsonData)</strong></code>: ส่งข้อมูลอุณหภูมิและความชื้นในรูปแบบ JSON ไปยังเซิร์ฟเวอร์</li></ul><ul id="10910dc0-8ab0-8025-8a3d-f33d2078ac98" class="bulleted-list"><li style="list-style-type:disc"><code><strong>delay(10000)</strong></code>: หยุดการทำงานของ loop ชั่วคราวเป็นเวลา 10 วินาที</li></ul><h2 id="10910dc0-8ab0-80b8-9cca-ec9c751adc77" class=""><mark class="highlight-red">โค้ดโดยรวม<br/><br/></mark></h2><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-8020-9ead-ff2702f271e2" class="code"><code class="language-C">#include &lt;WiFi.h&gt;
#include &lt;HTTPClient.h&gt;
#include &quot;DHT.h&quot;
#define DHTPIN 2  // กำหนดขาให้กับ DHT
#define DHTTYPE DHT22  // ใช้ DHT22 หรือ DHT11
DHT dht(DHTPIN, DHTTYPE);
const char* ssid = &quot;Saranphat&quot;; // ใส่ชื่อ WiFi ของคุณ
const char* password = &quot;123456789&quot;; // ใส่รหัสผ่าน WiFi ของคุณ
String serverIP = &quot;172.20.10.7&quot;; // ที่อยู่ local IP ของเซิร์ฟเวอร์ Python
void setup() {
  Serial.begin(115200);
  dht.begin();
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println(&quot;Connecting to WiFi...&quot;);
  }
  Serial.println(&quot;WiFi connected.&quot;);
  Serial.print(&quot;ESP32 IP address: &quot;);
  Serial.println(WiFi.localIP());  // แสดง IP Address ของ ESP32 ที่เชื่อมต่อ
}
void loop() {
  float temp = dht.readTemperature();
  float humid = dht.readHumidity();
  if (isnan(temp) || isnan(humid)) {
    Serial.println(&quot;Failed to read from DHT sensor!&quot;);
    return;
  }
  // แสดงค่าอุณหภูมิและความชื้น
  Serial.print(&quot;Temperature: &quot;);
  Serial.print(temp);
  Serial.println(&quot;°C&quot;);
  Serial.print(&quot;Humidity: &quot;);
  Serial.print(humid);
  Serial.println(&quot;%&quot;);
  // ส่งค่าไปยังเซิร์ฟเวอร์ที่ใช้ Python สำหรับ Discord Bot
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String serverURL = &quot;http://&quot; + serverIP + &quot;:5000/update&quot;; 
    http.begin(serverURL);
    http.addHeader(&quot;Content-Type&quot;, &quot;application/json&quot;);
    String jsonData = &quot;{\&quot;temp\&quot;: &quot; + String(temp) + &quot;, \&quot;humid\&quot;: &quot; + String(humid) + &quot;}&quot;;
    int httpResponseCode = http.POST(jsonData);
    Serial.print(&quot;HTTP Response code: &quot;);
    Serial.println(httpResponseCode);
    http.end();
  }
  delay(10000); // อัปเดตทุกๆ 10 วินาที (ปรับเปลี่ยนตามที่คุณต้องการ)
}</code></pre></div><div id="130fc48e-27d1-4e08-9a4a-ac9fb53925d3" style="width:50.00000000000004%" class="column"><h2 id="113aedc8-5567-4f35-8f14-aad9d9004e93" class=""><mark class="highlight-orange">Python Code</mark></h2><h3 id="10910dc0-8ab0-80b5-86e4-f41d83e67cd0" class="">การนำเข้าไลบรารี</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-8050-87f3-f526d11e6b00" class="code"><code class="language-Python">import discord
from discord.ext import commands
from flask import Flask, request, jsonify
import threading
//pip install discord.py Flask transformers command install</code></pre><ul id="10910dc0-8ab0-8096-bc83-fec435a167be" class="bulleted-list"><li style="list-style-type:disc"><code><strong>discord</strong></code>: ไลบรารีสำหรับสร้าง Discord Bot</li></ul><ul id="8fd4e454-adfb-48f9-8b10-1b2deb64fee9" class="bulleted-list"><li style="list-style-type:disc"><code><strong>commands</strong></code>: โมดูลที่ช่วยให้การจัดการคำสั่งในบอทง่ายขึ้น</li></ul><ul id="10910dc0-8ab0-8024-ab97-ed42b33df5aa" class="bulleted-list"><li style="list-style-type:disc"><code><strong>Flask</strong></code>: ไลบรารีสำหรับสร้างเว็บแอปพลิเคชันที่สามารถรับข้อมูล HTTP</li></ul><ul id="5d8c8b04-3be4-487d-96a5-31d492fdc97d" class="bulleted-list"><li style="list-style-type:disc"><code><strong>threading</strong></code>: ใช้สำหรับสร้าง thread ใหม่ เพื่อให้ Flask และ Discord Bot ทำงานพร้อมกัน</li></ul><h3 id="ba25067f-6fb6-4c93-8bf9-0ccba1b445ad" class="">2. ค่าคอนฟิกสำหรับ Discord</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-8011-9821-cb71b8adad3d" class="code"><code class="language-Python" style="white-space:pre-wrap;word-break:break-all">DISCORD_TOKEN = &#x27;YOUR_DISCORD_TOKEN&#x27;  # ใส่ Token ของ Discord Bot ของคุณที่นี่</code></pre><ul id="53836e47-2997-4e36-8448-2c69c610923c" class="bulleted-list"><li style="list-style-type:disc"><code><strong>DISCORD_TOKEN</strong></code>: ตัวแปรที่เก็บ Token สำหรับเข้าถึง Discord Bot ของคุณ (ควรเก็บเป็นความลับ)</li></ul><h3 id="ac015b76-8dc5-44b4-acb1-aaaaf8ff9d4c" class="">3. การสร้าง Flask App</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="320ddae2-8893-412d-aa33-c39747183475" class="code"><code class="language-Python" style="white-space:pre-wrap;word-break:break-all"> 
app = Flask(__name__)

temperature = None
humidity = None

</code></pre><ul id="77ddaf94-0480-482d-8792-af39e051890b" class="bulleted-list"><li style="list-style-type:disc"><code><strong>app = Flask(__name__)</strong></code>: สร้างแอปพลิเคชัน Flask</li></ul><ul id="10910dc0-8ab0-8041-b151-fb8477cb9054" class="bulleted-list"><li style="list-style-type:disc"><code><strong>temperature</strong></code><strong> และ </strong><code><strong>humidity</strong></code>: ตัวแปรที่ใช้เก็บค่าอุณหภูมิและความชื้นที่รับมาจาก ESP32 โดยเริ่มต้นเป็น <code>None</code></li></ul><h3 id="44193839-e7b8-40e1-a06a-b74653ac27e2" class="">4. Route สำหรับรับข้อมูลจาก ESP32</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-809e-9db8-f058e78d6756" class="code"><code class="language-Python" style="white-space:pre-wrap;word-break:break-all"> 
@app.route(&#x27;/update&#x27;, methods=[&#x27;POST&#x27;])
def update_sensor_data():
    global temperature, humidity
    try:
        data = request.json
        temperature = data.get(&#x27;temp&#x27;)
        humidity = data.get(&#x27;humid&#x27;)
        print(f&quot;Received temperature: {temperature}&quot;)
        print(f&quot;Received humidity: {humidity}&quot;)
        if temperature is None or humidity is None:
            return jsonify({&#x27;status&#x27;: &#x27;error&#x27;, &#x27;message&#x27;: &#x27;Invalid data format&#x27;}), 400
        return jsonify({&#x27;status&#x27;: &#x27;success&#x27;})
    except Exception as e:
        print(f&quot;Error: {e}&quot;)
        return jsonify({&#x27;status&#x27;: &#x27;error&#x27;, &#x27;message&#x27;: &#x27;Failed to process data&#x27;}), 500

</code></pre><ul id="10910dc0-8ab0-80c6-b299-f08ef5742c88" class="bulleted-list"><li style="list-style-type:disc"><code><strong>@app.route(&#x27;/update&#x27;, methods=[&#x27;POST&#x27;])</strong></code>: กำหนด route <code>/update</code> สำหรับรับข้อมูลแบบ POST</li></ul><ul id="10910dc0-8ab0-8067-abf3-c8b1104ec0de" class="bulleted-list"><li style="list-style-type:disc"><code><strong>update_sensor_data</strong></code>: ฟังก์ชันที่ทำงานเมื่อมีการส่งข้อมูลมาที่ <code>/update</code><ul id="10910dc0-8ab0-80ca-8b2f-ec72f3eae07a" class="bulleted-list"><li style="list-style-type:circle"><code><strong>request.json</strong></code>: รับข้อมูล JSON จาก HTTP request</li></ul><ul id="10910dc0-8ab0-80bf-bc84-ce3eda5d6271" class="bulleted-list"><li style="list-style-type:circle"><code><strong>temperature</strong></code><strong> และ </strong><code><strong>humidity</strong></code>: เก็บค่าจากข้อมูลที่ได้รับ</li></ul><ul id="10910dc0-8ab0-801d-bcde-d6e43db3ab08" class="bulleted-list"><li style="list-style-type:circle"><code><strong>print</strong></code>: แสดงค่าที่รับมาทาง console</li></ul><ul id="10910dc0-8ab0-8066-b77f-d773acb83ed5" class="bulleted-list"><li style="list-style-type:circle"><strong>การตรวจสอบข้อมูล</strong>: หากค่าที่ได้รับเป็น <code>None</code> จะส่งกลับข้อความแสดงข้อผิดพลาด</li></ul></li></ul><h3 id="10910dc0-8ab0-80b4-a171-c489764da056" class="">5. สร้าง Discord Bot</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-802a-ba88-d0d3fe4f16c0" class="code"><code class="language-Python" style="white-space:pre-wrap;word-break:break-all">intents = discord.Intents.default()
intents.message_content = True  # เปิดใช้งาน Intent สำหรับข้อความ
bot = commands.Bot(command_prefix=&#x27;$&#x27;, intents=intents)</code></pre><ul id="10910dc0-8ab0-8013-88a8-c704af01dff4" class="bulleted-list"><li style="list-style-type:disc"><code><strong>intents</strong></code>: กำหนดความสามารถของ Bot เช่น การอ่านข้อความที่ผู้ใช้ส่ง</li></ul><ul id="4a1bd671-05a3-4ec6-bc61-35037ebfef67" class="bulleted-list"><li style="list-style-type:disc"><code><strong>bot</strong></code>: สร้าง Bot โดยกำหนด prefix สำหรับคำสั่ง (ในที่นี้คือ <code>$</code>)</li></ul><h3 id="7707c78f-1432-4c54-93dc-8bd65b3c868b" class="">6. คำสั่งสำหรับ Discord Bot</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-808c-8bfc-e2101c74de05" class="code"><code class="language-Python" style="white-space:pre-wrap;word-break:break-all">@bot.command()
async def temp(ctx):
    if temperature is not None:
        try:
            temperature_float = float(temperature)
            temperature_formatted = f&quot;{temperature_float:.1f}&quot;
            await ctx.send(f&quot;Current temperature: {temperature_formatted}°C 🌡️&quot;)
        except ValueError:
            await ctx.send(&quot;Invalid temperature value.&quot;)
    else:
        await ctx.send(&quot;No temperature data available.&quot;)
@bot.command()
async def humid(ctx):
    if humidity is not None:
        humidity_int = round(humidity)
        await ctx.send(f&quot;Current humidity: {humidity_int}% 💧&quot;)
    else:
        await ctx.send(&quot;No humidity data available.&quot;)</code></pre><ul id="10910dc0-8ab0-802a-82e6-c63761c1ca95" class="bulleted-list"><li style="list-style-type:disc"><code><strong>@bot.command()</strong></code>: กำหนดคำสั่งที่สามารถเรียกใช้ได้ใน Discord</li></ul><ul id="2b3a8f30-1fa4-4843-beaa-9ca322afd903" class="bulleted-list"><li style="list-style-type:disc"><code><strong>temp(ctx)</strong></code>: แสดงค่าอุณหภูมิ</li></ul><ul id="10910dc0-8ab0-80be-a0e3-d01c476550db" class="bulleted-list"><li style="list-style-type:disc"><code><strong>humid(ctx)</strong></code>: แสดงค่าความชื้น</li></ul><ul id="10910dc0-8ab0-8081-ad95-f02fbe6283af" class="bulleted-list"><li style="list-style-type:disc"><code><strong>ctx.send()</strong></code>: ส่งข้อความตอบกลับไปยัง Discord Channel ที่มีการเรียกใช้คำสั่ง</li></ul><h3 id="10910dc0-8ab0-8063-be76-fc5e01e96e33" class="">7. การรัน Flask และ Discord Bot</h3><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-803e-bc93-e5daef74031d" class="code"><code class="language-Python" style="white-space:pre-wrap;word-break:break-all">if __name__ == &#x27;__main__&#x27;:
    def run_flask():
        app.run(host=&#x27;0.0.0.0&#x27;, port=5000)
    threading.Thread(target=run_flask).start()
    bot.run(DISCORD_TOKEN)</code></pre><ul id="10910dc0-8ab0-80d4-97cd-d5a9c6e6fa6c" class="bulleted-list"><li style="list-style-type:disc"><code><strong>if __name__ == &#x27;__main__&#x27;:</strong></code>: ตรวจสอบว่าโค้ดกำลังถูกเรียกใช้โดยตรง</li></ul><ul id="10910dc0-8ab0-80ed-ba6b-fbe138a67dbf" class="bulleted-list"><li style="list-style-type:disc"><code><strong>run_flask()</strong></code>: ฟังก์ชันที่ใช้เรียก Flask server โดยเปิดให้เข้าถึงจากทุก IP ที่อยู่ในเครือข่าย</li></ul><ul id="10910dc0-8ab0-80db-96e8-e203cfa629df" class="bulleted-list"><li style="list-style-type:disc"><code><strong>threading.Thread(target=run_flask).start()</strong></code>: เริ่ม thread ใหม่เพื่อให้ Flask server ทำงานพร้อมกันกับ Discord Bot</li></ul><ul id="10910dc0-8ab0-80cd-af74-d78a5a627939" class="bulleted-list"><li style="list-style-type:disc"><code><strong>bot.run(DISCORD_TOKEN)</strong></code>: เริ่ม Discord Bot โดยใช้ Token ที่กำหนด</li></ul><h2 id="10910dc0-8ab0-803f-b35d-c2339603f19e" class=""><mark class="highlight-red">โด้ดโดยรวมทั้งหมด</mark></h2><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="10910dc0-8ab0-8004-b49c-c6ecb969e511" class="code"><code class="language-Python">import discord
from discord.ext import commands
from flask import Flask, request, jsonify
import threading


DISCORD_TOKEN = &#x27;YOUR_DISCORD_TOKEN&#x27;  # ใส่ Token ของ Discord Bot ของคุณที่นี่

# สร้าง Flask App สำหรับรับข้อมูลจาก ESP32
app = Flask(__name__)

temperature = None
humidity = None

@app.route(&#x27;/update&#x27;, methods=[&#x27;POST&#x27;])
def update_sensor_data():
    global temperature, humidity
    try:
        data = request.json
        temperature = data.get(&#x27;temp&#x27;)
        humidity = data.get(&#x27;humid&#x27;)
        # ตรวจสอบข้อมูลที่ได้รับ
        print(f&quot;Received temperature: {temperature}&quot;)
        print(f&quot;Received humidity: {humidity}&quot;)
        if temperature is None or humidity is None:
            return jsonify({&#x27;status&#x27;: &#x27;error&#x27;, &#x27;message&#x27;: &#x27;Invalid data format&#x27;}), 400
        return jsonify({&#x27;status&#x27;: &#x27;success&#x27;})
    except Exception as e:
        print(f&quot;Error: {e}&quot;)
        return jsonify({&#x27;status&#x27;: &#x27;error&#x27;, &#x27;message&#x27;: &#x27;Failed to process data&#x27;}), 500

# สร้าง Discord Bot
intents = discord.Intents.default()
intents.message_content = True  # เปิดใช้งาน Intent สำหรับข้อความ
bot = commands.Bot(command_prefix=&#x27;$&#x27;, intents=intents)

@bot.command()
async def temp(ctx):
    if temperature is not None:
        try:
            temperature_float = float(temperature)
            temperature_formatted = f&quot;{temperature_float:.1f}&quot;
            await ctx.send(f&quot;Current temperature: {temperature_formatted}°C 🌡️&quot;)
        except ValueError:
            await ctx.send(&quot;Invalid temperature value.&quot;)
    else:
        await ctx.send(&quot;No temperature data available.&quot;)

@bot.command()
async def humid(ctx):
    if humidity is not None:
        # แสดงความชื้นด้วยจำนวนเต็ม
        humidity_int = round(humidity)
        await ctx.send(f&quot;Current humidity: {humidity_int}% 💧&quot;)
    else:
        await ctx.send(&quot;No humidity data available.&quot;)

if __name__ == &#x27;__main__&#x27;:
    # เริ่ม Flask server สำหรับรับข้อมูลจาก ESP32
    def run_flask():
        app.run(host=&#x27;0.0.0.0&#x27;, port=5000)

    threading.Thread(target=run_flask).start()

    # เริ่ม Discord bot
    bot.run(DISCORD_TOKEN)
</code></pre></div></div><p id="46543974-715f-4adc-863d-76cf43164a44" class="">
</p></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>
