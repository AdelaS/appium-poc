IF NOT EXIST "env" (
	virtualenv env --system-site-packages
)

call env\Scripts\activate
cmd