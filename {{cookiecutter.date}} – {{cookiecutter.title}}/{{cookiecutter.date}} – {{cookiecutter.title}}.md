<style>
@import url('./css/normalize.css');
@import url('./css/normbrief.css');
</style>

###### {{ cookiecutter.author_full_name }}
###### {{ cookiecutter.author_postal_address | join(' | ') }}
###### {% if cookiecutter.author_phone_number %}Tel. {{ cookiecutter.author_phone_number }}{% if cookiecutter.author_email_address %} | {% endif %}{% endif %}{{ cookiecutter.author_email_address }}
<br/>

###### {{ cookiecutter.author_full_name }} | {{ cookiecutter.author_postal_address | join(' | ') }}

{{ cookiecutter.recipient_full_name }}  
{{ cookiecutter.recipient_postal_address | join('  \n') }}  
<br/>
<br/>
<br/>
{% now 'local', '%d.%m.%Y' %}  
<br/>
**__Betreff__**  
<br/>  
__Inhalt__

Freundliche Grüße  
<br/><br/>
{{ cookiecutter.author_full_name }}
