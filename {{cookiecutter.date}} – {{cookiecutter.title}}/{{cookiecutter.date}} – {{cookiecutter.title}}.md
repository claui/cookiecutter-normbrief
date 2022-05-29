<style>
@import url('./css/normalize.css');
@import url('./css/normbrief.css');
</style>

###### {{ cookiecutter.author_full_name }}
###### {{ cookiecutter.author_letterhead_postal_address.split().join(' | ') }}
###### Tel. {{ cookiecutter.author_letterhead_phone_number }} | {{ cookiecutter.author_letterhead_email_address }}
<br/>

###### {{ cookiecutter.author_full_name }} | {{ cookiecutter.author_letterhead_postal_address.split().join(' | ') }}

{{ cookiecutter.recipient_full_name }}  
{{ cookiecutter.recipient_postal_address.split().join('  \n') }}  
<br/>
<br/>
<br/>
{{% now 'local', '%d.%m.%Y' %}}  
<br/>
**__Betreff__**  
<br/>  
__Inhalt__

Freundliche Grüße  
<br/><br/>
{{ cookiecutter.author_full_name }}
