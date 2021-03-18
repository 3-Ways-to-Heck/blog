## Wave a flag
#### Authored by Ethan Evans

TODO: Image

Here we are given one file, `warm`, an ELF executable. This means If you are using windows, you will need to either get this file onto a *nix system/VM or use the provided webshell using `wget`, `curl`, or the like.

Running the file prints a message saying to pass the argument `-h`. And there we have the flag.

```shell
> ./warm 
Hello user! Pass me a -h to learn what I can do!

> ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_6635aa47}
```

```
picoCTF{b1scu1ts_4nd_gr4vy_6635aa47}
```