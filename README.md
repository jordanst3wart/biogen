# biogen

Generate your versent bio from YAML using the latest template

## Installing

**Requires python3**

To install globally:

```
pip3 install git+ssh://git@github.com/Versent/biogen.git@master
```

`biogen` should now be on your $PATH to run from anywhere.

## Create a new bio

```
$ biogen create consultant
```

or

```
$ biogen create vms
```

Edit `my_versent_bio/biogen.yaml` and update `my_versent_bio/portrait.jpg` with your greyscale portrait.

Generate your bio!

```
$ cd my_versent_bio
$ biogen
Generated Andrew Ivins - Lead Engineer.docx
```

Open the resulting .docx file in Word to make sure it looks ok.