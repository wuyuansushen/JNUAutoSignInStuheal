# JNUAutoSignInStuheal
An auto student heath Sign in tools of JNU universary

## 1.Install *google-chrome-stable_current_x86_64.rpm*

```
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
