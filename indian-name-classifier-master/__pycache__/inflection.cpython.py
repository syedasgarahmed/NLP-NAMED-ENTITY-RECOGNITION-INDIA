 a

    ×wc`J+  ã                   @   sô   d Z ddlZddlZdZg d¢Zg d¢Zeg d¢ƒZdd„ Zd3d
d„Z	dd
„ Z
dd„ Zdd„ Zdd„ Z
d4dd„Zdd„ Zdd„ Zdd„ Zdd„ Zdd „ Zd!d"„ Zed#d$ƒ ed%d&ƒ ed'd(ƒ ed)d*ƒ ed+d,ƒ ed-d.ƒ ed/d0ƒ ed1d2ƒ dS )5z¶
    inflection
    ~~~~~~~~~~~~

    A port of Ruby on Rails' inflector to Python.

    :copyright: (c) 2012-2015 by Janne Vanhala

    :license: MIT, see LICENSE for more details.
é    Nz0.3.1))z(?i)(quiz)$z\1zes)z(?i)^(oxen)$ú\1)z
(?i)^(ox)$z\1en)ú
(?i)(m|l)ice$ú\1ice)z(?i)(m|l)ouse$r   )z(?i)(matr|vert|ind)(?:ix|ex)$z\1ices)z(?i)(x|ch|ss|sh)$ú\1es)z(?i)([^aeiouy]|qu)y$z\1ies)z(?i)(hive)$z\1s)z(?i)([lr])f$ú\1ves)z
(?i)([^f])fe$r   )z(?i)sis$Úses)ú(?i)([ti])a$ú\1a)z
(?i)([ti])um$r	   )z(?i)(buffal|potat|tomat)o$z\1oes)z
(?i)(bu)s$z\1ses)z(?i)(alias|status)$r   )z(?i)(octop|vir)i$ú\1i)z(?i)(octop|vir)us$r
   )z(?i)^(ax|test)is$r   )ú(?i)s$Ús)ú$r   ) )z(?i)(database)s$r   )z(?i)(quiz)zes$r   )z(?i)(matr)ices$z\1ix)z(?i)(vert|ind)ices$z\1ex)z(?i)^(ox)enr   )z(?i)(alias|status)(es)?$r   )z(?i)(octop|vir)(us|i)$z\1us)z(?i)^(a)x[ie]s$z\1xis)z(?i)(cris|test)(is|es)$z\1is)z(?i)(shoe)s$r   )z
(?i)(o)es$r   )z(?i)(bus)(es)?$r   )r   z\1ouse)z(?i)(x|ch|ss|sh)es$r   )z
(?i)(m)ovies$z\1ovie)z
(?i)(s)eries$z\1eries)z(?i)([^aeiouy]|qu)ies$z\1y)z(?i)([lr])ves$z\1f)z(?i)(tive)s$r   )z(?i)(hive)s$r   )z(?i)([^f])ves$z\1fe)z(?i)(t)he(sis|ses)$z\1hesis)z(?i)(s)ynop(sis|ses)$z	\1ynopsis)z(?i)(p)rogno(sis|ses)$z
\1rognosis)z(?i)(p)arenthe(sis|ses)$z\1arenthesis)z(?i)(d)iagno(sis|ses)$z
\1iagnosis)z(?i)(b)a(sis|ses)$z\1asis)z(?i)(a)naly(sis|ses)$z	\1nalysis)r   z\1um)z(?i)(n)ews$z\1ews)z	(?i)(ss)$r   )r   Ú )	Z	equipmentÚfishÚinformationZjeansZmoneyÚriceÚseriesÚsheepZspeciesc              	   C   s8  dd„ }| d   ¡ |d   ¡ kr´t dd| d | dd… f d|dd…  f¡ t dd|d |dd… f d|dd…  f¡ t dd|d |dd… f d| dd…  f¡ n€t dd| d   ¡ || dd… ƒf |d   ¡ |dd…  f¡ t dd| d  ¡ || dd… ƒf |d  ¡ |dd…  f¡ t dd|d   ¡ ||dd… ƒf |d   ¡ |dd…  f¡ t dd|d  ¡ ||dd… ƒf |d  ¡ |dd…  f¡ t dd|d   ¡ ||dd… ƒf | d   ¡ | dd…  f¡ t dd|d  ¡ ||dd… ƒf | d  ¡ | dd…  f¡ dS )	zÑ
    A convenience function to add appropriate rules to plurals and singular
    for irregular words.

    :param singular: irregular word in singular form
    :param plural: irregular word in plural form
    c                 S   s   d  dd„ | D ƒ¡S )Nr   c                 s   s"   | ]}d | |  ¡  d V  qdS )Ú[Ú]N)Úupper)Ú.0Úchar© r   úaC:\Users\Syed Asgar\NLP\indian-name-classifier-master\indian-name-classifier-master\inflection.pyÚ	<genexpr>c   ó    z6_irregular.<locals>.caseinsensitive.<locals>.<genexpr>)Újoin)Ústringr   r   r   Úcaseinsensitiveb   s    z#_irregular.<locals>.caseinsensitiver   z(?i)(%s)%s$é   Nr   z%s%s$)r   ÚPLURALSÚinsertÚ	SINGULARSÚlower)ÚsingularÚpluralr   r   r   r   Ú
_irregularZ   sL    þþþ
þþþþþþr'   Tc                 C   s6   |rt  ddd„ | ¡S | d  ¡ t| ƒdd…  S dS )a?  
    Convert strings to CamelCase.

    Examples::

        >>> camelize("device_type")
        "DeviceType"
        >>> camelize("device_type", False)
        "deviceType"

    :func:`camelize` can be though as a inverse of :func:`underscore`, although
    there are some cases where that does not hold::

        >>> camelize(underscore("IOError"))
        "IoError"

    :param uppercase_first_letter: if set to `True` :func:`camelize` converts
        strings to UpperCamelCase. If set to `False` :func:`camelize` produces
        lowerCamelCase. Defaults to `True`.
    z
(?:^|_)(.)c                 S   s   |   d¡ ¡ S ©Nr    ©Úgroupr   ©Úmr   r   r   Ú<lambda>£   r   zcamelize.<locals>.<lambda>r   r    N)ÚreÚsubr$   Úcamelize)r   Zuppercase_first_letterr   r   r   r0      s    r0   c                 C   s   |   dd¡S )z{Replace underscores with dashes in the string.

    Example::

        >>> dasherize("puni_puni")
        "puni-puni"

    Ú_ú-)Úreplace©Úwordr   r   r   Ú	dasherize¨   s    	r6   c                 C   sB   t  dd| ¡} |  dd¡} t  ddd„ | ¡} t  dd	d„ | ¡} | S )
a<  
    Capitalize the first word and turn underscores into spaces and strip a
    trailing ``"_id"``, if any. Like :func:`titleize`, this is meant for
    creating pretty output.

    Examples::

        >>> humanize("employee_salary")
        "Employee salary"
        >>> humanize("author_id")
        "Author"

    z_id$r   r1   ú z(?i)([a-z\d]*)c                 S   s   |   d¡ ¡ S r(   )r*   r$   r+   r   r   r   r-   Ä   r   zhumanize.<locals>.<lambda>z^\wc                 S   s   |   d¡ ¡ S )Nr   r)   r+   r   r   r   r-   Å   r   )r.   r/   r3   r4   r   r   r   Úhumanize´   s
    r8   c                 C   s8   t t| ƒƒ} | d dv rdS ddddœ | d d¡S d	S )
a€  
    Return the suffix that should be added to a number to denote the position
    in an ordered sequence such as 1st, 2nd, 3rd, 4th.

    Examples::

        >>> ordinal(1)
        "st"
        >>> ordinal(2)
        "nd"
        >>> ordinal(1002)
        "nd"
        >>> ordinal(1003)
        "rd"
        >>> ordinal(-11)
        "th"
        >>> ordinal(-1021)
        "st"

    éd   )é   é   é
   ÚthÚstÚndÚrd)r    é   é   é
   N)ÚabsÚintÚget©Únumberr   r   r   ÚordinalÉ   s    ýürI   c                 C   s   d| t | ƒf S )a›  
    Turn a number into an ordinal string used to denote the position in an
    ordered sequence such as 1st, 2nd, 3rd, 4th.

    Examples::

        >>> ordinalize(1)
        "1st"
        >>> ordinalize(2)
        "2nd"
        >>> ordinalize(1002)
        "1002nd"
        >>> ordinalize(1003)
        "1003rd"
        >>> ordinalize(-11)
        "-11th"
        >>> ordinalize(-1021)
        "-1021st"

    z%s%s)rI   rG   r   r   r   Ú
ordinalizeé   s    rJ   r2   c                 C   sT   t | ƒ} t d|| ¡} |rLt |¡}t d| || ¡} t dd|i d| ¡} |  ¡ S )z½
    Replace special characters in a string so that it may be used as part of a
    'pretty' URL.

    Example::

        >>> parameterize(u"Donald E. Knuth")
        'donald-e-knuth'

    z(?i)[^a-z0-9\-_]+z%s{2,}z(?i)^%(sep)s|%(sep)s$Úsepr   )Ú
transliterater.   r/   Úescaper$   )r   Ú	separatorZre_sepr   r   r   Úparameterize  s    
rO   c                 C   sH   | r|   ¡ tv r| S tD ]&\}}t || ¡rt ||| ¡  S q| S dS )a  
    Return the plural form of a word.

    Examples::

        >>> pluralize("post")
        "posts"
        >>> pluralize("octopus")
        "octopi"
        >>> pluralize("sheep")
        "sheep"
        >>> pluralize("CamelOctopus")
        "CamelOctopi"

    N)r$   ÚUNCOUNTABLESr!   r.   Úsearchr/   )r5   ÚruleÚreplacementr   r   r   Ú	pluralize  s    rT   c                 C   sR   t D ]}t d| | ¡r|   S qtD ]&\}}t || ¡r&t ||| ¡  S q&| S )ac  
    Return the singular form of a word, the reverse of :func:`pluralize`.

    Examples::

        >>> singularize("posts")
        "post"
        >>> singularize("octopi")
        "octopus"
        >>> singularize("sheep")
        "sheep"
        >>> singularize("word")
        "word"
        >>> singularize("CamelOctopi")
        "CamelOctopus"

    z(?i)\b(%s)\Z)rP   r.   rQ   r#   r/   )r5   Ú
inflectionrR   rS   r   r   r   Úsingularize2  s    
rV   c                 C   s   t t| ƒƒS )as  
    Create the name of a table like Rails does for models to table names. This
    method uses the :func:`pluralize` method on the last word in the string.

    Examples::

        >>> tableize('RawScaledScorer')
        "raw_scaled_scorers"
        >>> tableize('egg_and_ham')
        "egg_and_hams"
        >>> tableize('fancyCategory')
        "fancy_categories"
    )rT   Ú
underscorer4   r   r   r   ÚtableizeN  s    rX   c                 C   s   t  ddd„ tt| ƒƒ¡S )aé  
    Capitalize all the words and replace some characters in the string to
    create a nicer looking title. :func:`titleize` is meant for creating pretty
    output.

    Examples::

      >>> titleize("man from the boondocks")
      "Man From The Boondocks"
      >>> titleize("x-men: the last stand")
      "X Men: The Last Stand"
      >>> titleize("TheManWithoutAPast")
      "The Man Without A Past"
      >>> titleize("raiders_of_the_lost_ark")
      "Raiders Of The Lost Ark"

    z\b('?[a-z])c                 S   s   |   d¡ ¡ S r(   )r*   Ú
capitalize)Úmatchr   r   r   r-   s  r   ztitleize.<locals>.<lambda>)r.   r/   r8   rW   r4   r   r   r   Útitleize_  s
    
ýr[   c                 C   s   t  d| ¡}| dd¡ d¡S )u9  
    Replace non-ASCII characters with an ASCII approximation. If no
    approximation exists, the non-ASCII character is ignored. The string must
    be ``unicode``.

    Examples::

        >>> transliterate(u'Ã¤lÃ¤mÃ¶lÃ¶')
        u'alamolo'
        >>> transliterate(u'Ã†rÃ¸skÃ¸bing')
        u'rskbing'

    ÚNFKDÚasciiÚignore)ÚunicodedataÚ	normalizeÚencodeÚdecode)r   Ú
normalizedr   r   r   rL   x  s    rL   c                 C   s0   t  dd| ¡} t  dd| ¡} |  dd¡} |  ¡ S )aq  
    Make an underscored, lowercase form from the expression in the string.

    Example::

        >>> underscore("DeviceType")
        "device_type"

    As a rule of thumb you can think of :func:`underscore` as the inverse of
    :func:`camelize`, though there are cases where that does not hold::

        >>> camelize(underscore("IOError"))
        "IoError"

    z([A-Z]+)([A-Z][a-z])z\1_\2z([a-z\d])([A-Z])r2   r1   )r.   r/   r3   r$   r4   r   r   r   rW   Š  s    rW   ÚpersonÚpeopleÚmanZmenÚhumanZhumansÚchildÚchildrenZsexZsexesÚmoveÚmovesÚcowZkineÚzombieZzombies)T)r2   )Ú__doc__r.   r_   Ú__version__r!   r#   ÚsetrP   r'   r0   r6   r8   rI   rJ   rO   rT   rV   rX   r[   rL   rW   r   r   r   r   Ú<module>   s6   
#
3
 








