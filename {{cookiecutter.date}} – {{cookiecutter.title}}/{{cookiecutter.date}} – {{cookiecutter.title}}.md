<!-- markdownlint-configure-file {
  "MD033": { "allowed_elements": ["br", "style"] },
  "MD041": false,
} -->

<style>
@import url('./css/normalize.css');
@import url('./css/normbrief.css');
</style>

<!-- markdownlint-disable MD022 -->
###### {{ cookiecutter.author_full_name }}
###### {{ cookiecutter.author_postal_address | join(' | ') }}
###### {% if cookiecutter.author_phone_number %}Tel. {{ cookiecutter.author_phone_number }}{% if cookiecutter.author_email_address %} | {% endif %}{% endif %}{{ cookiecutter.author_email_address }}
<!-- markdownlint-enable MD022 -->
<br/>

###### {{ cookiecutter.author_full_name }} | {{ cookiecutter.author_postal_address | join(' | ') }}

{{ cookiecutter.recipient_full_name }}  
{{ cookiecutter.recipient_postal_address | join('  \n') }}  
<br/>
<br/>
<br/>
{% now 'local', '%d.%m.%Y' %}  
<br/>
**<!-- Betreff -->**  
<br/>  
<!-- Inhalt -->

Freundliche Grüße  
<br/><br/>
{{ cookiecutter.author_full_name }}
