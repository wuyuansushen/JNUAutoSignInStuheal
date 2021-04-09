# JNUAutoSignInStuheal
An auto student heath Sign in tools of JNU universary

## 1.Install *google-chrome-stable_current_x86_64.rpm*

```
cd JNUAutoSignInStuheal/
dnf -y install ./google-chrome-stable_current_x86_64.rpm
```

## 2.Install *selenium* module

```
python3 -m pip install selenium
```
## 3.Extract *chromedriver*

```
unzip ./chromedriver_linux64.zip
```

>:warning: If you don't have `unzip`, run `dnf -y install unzip`.

## 4.Adding *chromedriver* to your `$PATH`
```
cp chromedriver /usr/local/bin/
```

## 5.Add Permission

```
chmod u+x signIn_stuhealth.py
```

## 6.Move to */usr/local/bin/*

```
cd ..
cp -r JNUAutoSignInStuheal /usr/local/bin/
```

## 7. (Optional) Add to `crontab`

```
(crontab -l;echo "0 3 * * * python3 /usr/local/bin/JNUAutoSignInStuheal/signIn_stuhealth.py") | crontab
```

>:warning: If you don't have `crontab`, run `dnf -y install cronie`.
